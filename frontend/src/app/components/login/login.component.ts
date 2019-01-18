import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router'
import { NgForm } from '@angular/forms';
import { AppError } from '../../common/validators/app-error';
import { NotFoundError } from '../../common/validators/not-found-error';
import { BadInput } from '../../common/validators/bad-input';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginUserData = {}
  err: any;

  constructor(private _auth: AuthService,
    private _router: Router) { }

  ngOnInit() {
  }

  loginUser(form: NgForm) {
    this._auth.loginUser(this.loginUserData)
      .subscribe(
        res => {
          console.log(res)
          localStorage.setItem('token', res.token)
          this._router.navigate(['/special'])
        },
        //  (error: AppError) =>{
        //   if (error instanceof NotFoundError) {
        //     console.log(error)
        //     this.err = error
        //   } 
        //   if (error instanceof BadInput) {
        //      // this.form.setErrors(error.originalError)
        //      console.log(error,"askdnkasn")
        //   }
        //   else throw error
        // }
      )
  }

}
