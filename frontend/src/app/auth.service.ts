import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Router } from '@angular/router';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Authorization': 'token'
  })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _registerUrl = "http://localhost:8000/api/v1/auth/jwt/register"
  private _loginUrl = "http://localhost:8000/api/v1/auth/jwt"
  
  
  constructor(private http: HttpClient, private _router: Router) {  }
  
  // createAuthorizationHeader(headers: HttpHeaders) {
  //   headers: new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     //'Authorization': 'my-auth-token'
  //   })
  // }
  

  registerUser(user): Observable<any> {
    return this.http.post<any>(this._registerUrl, user, httpOptions)
      .pipe(
        //catchError(this.handleError('addHero', hero))
      );
  }

  // loginUser(user): Observable<any> {
  //   return this.http.post<any>(this._loginUrl, JSON.stringify(user), httpOptions)
  //     .pipe(
  //       map(res => {
  //         let result = res.json()
  //         if (result && result.token){
  //           localStorage.setItem('token', result.token)
  //           return true
  //         }
  //         else return false
  //         })
  //     )
  // }

  // registerUser(user) {
  //   return this.http.post<any>(this._registerUrl, user)
  // }

  loginUser(user) {
    return this.http.post<any>(this._loginUrl, user, httpOptions)
  }

  logoutUser() {
    localStorage.removeItem('token')
    this._router.navigate(['/events'])
  }

  getToken() {
    return localStorage.getItem('token')
  }

  loggedIn() {
    return !!localStorage.getItem('token')
  }
  
  

}
