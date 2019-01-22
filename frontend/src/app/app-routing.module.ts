import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { AuthGuard } from './guards/auth.guard';
import { SoftwareListComponent } from './components/software-list/software-list.component';

const routes: Routes = [
  {
    path: '', redirectTo: '/software-list', pathMatch: 'full'
  },
  {
    path: 'software-list', canActivate: [AuthGuard], component: SoftwareListComponent
  },
  {
    path: 'login', component: LoginComponent
  },
  {
    path: 'register', component: RegisterComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
