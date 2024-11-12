const subject = new Quill('#content', {
    theme: 'snow',
    placeholder: 'hola ...',
});

const validate = (data) => {
    const schema = Joi.object({
        subject: Joi.string().min(3).required(),
        recipients: Joi.array().items(Joi.string().email()).required(),
        content: Joi.string().required()
    });
    return schema.validate(data);
}

export default (emailService) => {

    document.getElementById("emailForm").onsubmit = async (e) => {
        e.preventDefault()

        const form = new FormData(e.target)
        const data = Object.fromEntries(form.entries());
        data.recipients = data.recipients.split(";")
        data.content = subject.root.innerHTML

        const { error, value } = validate(data);

        if (!error) {
            await emailService.send(form)
        }

    };

}


