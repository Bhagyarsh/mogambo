import { AppError } from './app-error';

export class NotFoundError extends AppError {
    
    constructor(originalError: any) {
        super(originalError)
        originalError = "404 Not Found Error!"
        alert(originalError)
        console.log(originalError)
    }
}