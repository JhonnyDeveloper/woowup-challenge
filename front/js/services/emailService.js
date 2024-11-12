export class EmailService {

    #httpClient

    constructor(httpClient) {
        this.#httpClient = httpClient
    }

    async send(form) {
        const payload = {
            recipients: form.get("recipients").split(";"),
            subject: form.get("subject"),
            content: form.get("content"),
        };
        return await this.#httpClient.post(payload)
    }
}