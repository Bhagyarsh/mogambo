import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    // "Access-Control-Allow-Origin":"*",
    // "Access-Control-Allow-Methods":"GET, POST",
    //'Authorization': 'my-auth-token'
  })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _registerUrl = "http://127.0.0.1:8000/api/v1/auth/jwt/register"
  private _loginUrl = "http://127.0.0.1:8000/api/v1/auth/jwt/"

  
  constructor(private http: HttpClient) { }
  
  // createAuthorizationHeader(headers: HttpHeaders) {
  //   headers: new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     //'Authorization': 'my-auth-token'
  //   })
  // }


  // registerUser(user) {}
  //   return this.http.post<any>(this._registerUrl, user, {
  //     headers: headers
  //   })
  // }

  // registerUser(user) {
  //   let headers: any = new Headers();
  //   this.createAuthorizationHeader(headers);
  //   return this.http.post<any>(this._registerUrl, user, {
  //     headers: headers
  //   });
  // }
  registerUser(user): Observable<any> {

    return this.http.post<any>(this._registerUrl, user, httpOptions)
      .pipe(
        //catchError(this.handleError('addHero', hero))
      );
  }


  loginUser(user) {
    console.log(user);
    console.log('HHHHHHHHHH');
    return this.http.post<any>(this._loginUrl, user)
  }

  getToken() {
    return localStorage.getItem('token')
  }
}
