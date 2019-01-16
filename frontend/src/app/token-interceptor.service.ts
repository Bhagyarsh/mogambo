// import { Injectable, Injector } from '@angular/core';
// import {
//   HttpEvent, HttpInterceptor, HttpHandler, HttpRequest
// } from '@angular/common/http';

// import { tap } from 'rxjs/operators';
// import { Router } from "@angular/router";

// import { AuthService } from './auth.service';
// import { Observable } from 'rxjs';

// @Injectable({
//   providedIn: 'root'
// })
// export class TokenInterceptorService implements HttpInterceptor {

//   intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>>{
//     let authService = this.injector.get(AuthService)
//     if (authService.getToken()){
//       let tokenizedReq = req.clone(
//         {
//           headers: req.headers.set('Authorization', 'JWT ' + authService.getToken())
//         }
//       )
//       return next.handle(tokenizedReq)
//     }
//     else{
//       let tokenizedReq = req.clone(
//       )
//       return next.handle(tokenizedReq)
//     }
//   }
// }
