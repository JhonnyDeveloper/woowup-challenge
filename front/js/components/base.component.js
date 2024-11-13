export default class BaseComponent {
    constructor(notify) {
        this.notify = notify
    }

    showValidationErrors(error) {
        const _errors = error.details.map((detail) => `<li>${detail.message}</li>`)
        this.notify.error({
            message: `<ul>${_errors}</ul>`,
            duration: 9000,
            icon: false
        });
    }
}