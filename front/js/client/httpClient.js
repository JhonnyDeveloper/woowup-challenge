export class HttpClient {

    #url;
    #headers

    constructor(url, headers) {
        this.#url = url
        this.#headers = {
            'Content-Type': 'application/json',
            ...headers
        }
    }

    async post(payload) {
        const response = await fetch(
            this.#url,
            {
                method: "POST",
                headers: this.#headers,
                body: JSON.stringify(payload),
                mode: 'cors',
            }
        );
        if (!response.ok) {
            throw {
                status: response.status,
                message: response.statusText
            }

        }
        return await response.json();
    }
}