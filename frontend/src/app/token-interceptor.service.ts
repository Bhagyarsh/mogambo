import { Injectable, Injector } from '@angular/core';
import {
  HttpEvent, HttpInterceptor, HttpHandler, HttpRequest
} from '@angular/common/http';

import { AuthService } from './auth.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TokenInterceptorService implements HttpInterceptor {

  constructor(private injector: Injector) { }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>>{
    let authService = this.injector.get(AuthService)
<<<<<<< HEAD
    let tokenizedReq = req.clone(
      {
        headers: req.headers.set('Authorization', 'JWT ' + authService.getToken())
=======
    let tokenizedReq = req.clone({
      
      setHeaders: {
        'Content-Type': 'application/json',
        Authorization: `JWT ${authService.getToken()}`
>>>>>>> 5a94fe9704ffe9ec4a0f3d99d7ce2f084058008e
      }
    )
    return next.handle(tokenizedReq)
  }
}
