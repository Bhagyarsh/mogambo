import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    //'Authorization': 'my-auth-token'
  })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _registerUrl = "http://ptsv2.com/t/bhagyarsh/post"
  private _loginUrl = "http://ptsv2.com/t/bhagyarsh/post"

  
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
    return this.http.post<any>(this._loginUrl, user)
  }

  getToken() {
    return localStorage.getItem('token')
  }
}
