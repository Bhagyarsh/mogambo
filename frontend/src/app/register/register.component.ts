import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Userreg } from './model';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  registerUserData : Userreg = {}
 
  constructor(private _auth: AuthService) {  console.log(this.registerUserData)}

  ngOnInit() {console.log(this.registerUserData)
  }
  
  registerUser() {
    this._auth.registerUser(this.registerUserData)
      .subscribe(
        res => { 
          console.log(res)
          localStorage.setItem('token', res.token)
        },
        err => console.log(err) 
      )
  }

}
