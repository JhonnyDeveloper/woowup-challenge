import { ENV } from "../config/environment.js";
import { HttpClient } from "../client/httpClient.js";
import { EmailService } from "../services/email.service.js";

var notyf = new Notyf();
const httpClient = new HttpClient(ENV.api.email, {})
const emailService = new EmailService(httpClient)

export {
    emailService,
    notyf
};
