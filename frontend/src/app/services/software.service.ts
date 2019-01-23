import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Authorization': 'JWT token',
    'Accept': 'application/json'
  })
};


@Injectable({
  providedIn: 'root'
})
export class SoftwareService {

  private _listUrl = "http://127.0.0.1:8000/api/v1/software/"
  private _createUrl = "http://127.0.0.1:8000/api/v1/software/create"

constructor(public http: HttpClient) { }

getAll() {
  return this.http.get<any>(this._listUrl)
}

create(softwareData) {
  return this.http.post<any>(this._createUrl, softwareData, httpOptions)
    .pipe(
      //catchError(this.handleError)
    )
}

}
