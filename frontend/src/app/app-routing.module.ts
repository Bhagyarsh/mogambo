import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { EventsComponent } from './components/events/events.component';
import { AuthGuard } from './guards/auth.guard';
import { SpecialEventsComponent } from './components/special-events/special-events.component';

const routes: Routes = [
  {
    path: '', redirectTo: '/events', pathMatch: 'full'
  },
  {
    path: 'events', component: EventsComponent
  },
  {
    path: 'special', canActivate: [AuthGuard], component: SpecialEventsComponent
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
