import BaseComponent from "./base.component.js";

export default class EmailComponent extends BaseComponent {

    #EmailService
    #EmailSchama = Joi.object({
        subject: Joi.string().min(3).required(),
        recipients: Joi.array().items(Joi.string().email()).min(1).required(),
        content: Joi.string().required()
    });
    #Subject
    #Recipients

    constructor(notify, emailService) {
        super(notify)

        this.#EmailService = emailService;
        this.createSubject();
        this.createRecipients();
        this.start()
    }

    start() {
        document.getElementById("emailForm").onsubmit = async (event) => {
            event.preventDefault();
            await this.send(event)
        };
    }

    createSubject() {
        this.#Subject = new Quill('#content', {
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
        form.content = this.#Subject.root.innerHTML === "<p><br></p>" ? "" : this.#Subject.root.innerHTML;
        const { error } = this.#EmailSchama.validate(form);

        if (error) {
            this.showValidationErrors(error);
            return;
        }

        try {
            await this.#EmailService.send(form)
        } catch (error) {

        }
    }
}


