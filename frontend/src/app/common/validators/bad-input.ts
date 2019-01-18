import { AppError } from './app-error';

export class BadInput extends AppError {
    
    constructor(originalError:any) {
        super(originalError)
        // this.originalError = "Invalid email and password!"
        // alert(this.originalError)
        // console.log(this.originalError)
        
    }
    loginError(error: Response) {
        this.originalError = "Invaliddd email and password!"
        alert(this.originalError)
        console.log(this.originalError)
    }

    registerError(error: Response) {
        this.originalError = "Email is already registered, try something else!"
        alert(this.originalError)
        console.log(this.originalError)
    }
}