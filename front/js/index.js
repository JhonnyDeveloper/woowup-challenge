import { emailService, notyf } from './config/dependencies.js';
import EmailComponent from "./components/email.component.js";

const emailComponent = new EmailComponent(notyf, emailService)

