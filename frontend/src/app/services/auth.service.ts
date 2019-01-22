import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { Router } from '@angular/router';
import { AppError } from '../common/validators/app-error';
import { NotFoundError } from '../common/validators/not-found-error';
import { BadInput } from '../common/validators/bad-input';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    // 'Authorization': 'token',
    'Accept': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _registerUrl = "http://localhost:8000/api/v1/auth/jwt/register"
  private _loginUrl = "http://127.0.0.1:8000/api/v1/auth/jwt"
  
  
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
        catchError(this.handleError)
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


  loginUser(user) {
    return this.http.post<any>(this._loginUrl, user, httpOptions)
      .pipe(
        catchError(this.handleError)
      )
  }

  logoutUser() {
    localStorage.removeItem('token')
    this._router.navigate(['/login'])
  }

  getToken() {
    return localStorage.getItem('token')
  }

  loggedIn() {
    return !!localStorage.getItem('token')
  }

  private handleError(error: Response) {
    if (error.status === 404) {
      return throwError(new NotFoundError(error))
    }
    else if (error.url === "http://localhost:8000/api/v1/auth/jwt/register" && error.status === 400) {
      return throwError(new BadInput(error).registerError(error))
    }
    else if (error.url === "http://127.0.0.1:8000/api/v1/auth/jwt" && error.status === 400 ) {
      return throwError(new BadInput(error).loginError(error))
    }
    else { 
    return throwError(alert("unexpected error occurred!"))   
    }
  }
}
