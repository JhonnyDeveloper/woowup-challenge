import BaseComponent from "./base.component.js";

export default class EmailComponent extends BaseComponent {

    #EmailService
    #EmailSchama = Joi.object({
        subject: Joi.string().min(3).required(),
        recipients: Joi.array().items(Joi.string().email()).min(1).required(),
        content: Joi.string().required()
    });
    #Content
    #Recipients

    constructor(notify, emailService) {
        super(notify)

        this.#EmailService = emailService;
        this.createContent();
        this.createRecipients();
        this.start()
    }

    start() {
        document.getElementById("emailForm").onsubmit = async (event) => {
            event.preventDefault();
            await this.send(event)
        };
    }

    createContent() {
        this.#Content = new Quill('#content', {
            theme: 'snow',
            placeholder: 'Content',
        });
    }

    createRecipients() {
        this.#Recipients = new Tagify(document.getElementById('recipients'), {
            editTags: {
                keepInvalid: false,
            },
            pattern: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
            callbacks: {
                invalid: (error) => { this.notify.error("Invalid email") }
            }
        })
    }

    async send(event) {

        const form = Object.fromEntries(new FormData(event.target).entries());
        form.recipients = JSON.parse(form.recipients || "[]").map((recipient) => recipient.value)
        form.content = this.#Content.root.innerHTML === "<p><br></p>" ? "" : this.#Content.root.innerHTML;
        const { error } = this.#EmailSchama.validate(form);

        if (!error) {
            this.#EmailService.send(form).then((result) => {
                this.notify.success({
                    message: "Mail sent",
                    duration: 9000
                })
                this.cleanForm();
            }).catch((error) => {
                this.notify.error({
                    message: "The email was not sent, try again please",
                    duration: 9000
                })
            })
            return;
        }

        this.showValidationErrors(error);
    }

    cleanForm() {
        document.getElementById("emailForm").reset();
        this.#Recipients.removeAllTags()
        this.#Content.setContents([
            { insert: '' }
        ])
    }

}


