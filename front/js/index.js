import { ENV } from "./config/environment.js";
import { HttpClient } from "./client/httpClient.js";
import { EmailService } from "./services/emailService.js";
import emailComponent from "./emailComponent.js";

const httpService = new HttpClient(ENV.api.email, {})
const emailService = new EmailService(httpService)

emailComponent(emailService);

