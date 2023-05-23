import {Component} from '@angular/core';
import {ImagesHandlerService} from './shared/images-handler.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'front';
  protected readonly ImagesHandlerService = ImagesHandlerService;
}
