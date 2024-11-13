export class EmailService {

    #httpClient

    constructor(httpClient) {
        this.#httpClient = httpClient
    }

    async send(payload) {
        return await this.#httpClient.post(payload)
    }
}