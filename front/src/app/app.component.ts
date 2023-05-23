import {Component, OnInit} from '@angular/core';
import {ImagesHandlerService} from './shared/images-handler.service';
import * as d3 from 'd3';
import {DragAndDropComponent} from "./drag-and-drop/drag-and-drop.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'front';
  protected readonly ImagesHandlerService = ImagesHandlerService;

}

