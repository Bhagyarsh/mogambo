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

<<<<<<< HEAD
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>>{
    let authService = this.injector.get(AuthService)
    if (authService.getToken()){
      let tokenizedReq = req.clone(
        {
          headers: req.headers.set('Authorization', 'JWT ' + authService.getToken())
        }
      )
      return next.handle(tokenizedReq)
    }
    else{
      let tokenizedReq = req.clone(
      )
      return next.handle(tokenizedReq)
    }
  }
}
=======
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
  
>>>>>>> e1d2fce582f6d5f02af3443e4d63a464892ddf18
