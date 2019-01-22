import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router'
import { User } from '../../models/user.model';
import { AppError } from '../../common/validators/app-error';
import { BadInput } from '../../common/validators/bad-input';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  userData: User = {
    firstname : '',
    lastname : '',
    email : '',
    password : '',
  }

  constructor(private _auth: AuthService,
    private _router: Router) { }

  ngOnInit() {
  }

  registerUser() {
    this._auth.registerUser(this.userData)
      .subscribe(
        res => {
          console.log(res)
          localStorage.setItem('token', res.token)
          this._router.navigate(['/login'])
        },
        // (error: AppError) => {
        //   if (error instanceof BadInput)
        //     {
        //       alert("Email alreaady registered.")
        //       console.log(error)
        //     }
        //   else throw error
        // }
      )
  }


}
