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

//   constructor(private injector: Injector,
//               private router: Router) { }

//   intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
//     let authService = this.injector.get(AuthService)
//     if (req.headers.get('No-Auth') == "True")
//       return next.handle(req.clone());

//     if (localStorage.getItem('token') != null) {
//       const clonedreq = req.clone({
//         headers: req.headers.set("Authorization", "JWT " + localStorage.getItem('token'))
//       });
//       return next.handle(clonedreq)
//         .pipe(tap(
//           succ => { console.log(succ) },
//           err => {
//             if (err.status === 401)
//               this.router.navigateByUrl('/login');
//           }
//         ));
//     }
//     else {
//       this.router.navigateByUrl('/login');
//     }
//   }
// }
  
