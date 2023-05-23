import {Component, OnInit} from '@angular/core';
import {ImagesHandlerService} from './shared/images-handler.service';
import * as d3 from 'd3';
import {DragAndDropComponent} from "./drag-and-drop/drag-and-drop.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  title = 'front';
  protected readonly ImagesHandlerService = ImagesHandlerService;

  generateRandomGraph(): void {
    const graphContainer = d3.select('#graph');

    // Clear any existing graph
    graphContainer.selectAll('*').remove();

    // Generate random data for the graph
    const nodes = Array.from({length: 10}, (_, i) => ({id: i}));
    const links = Array.from({length: 10}, () => ({
      source: Math.floor(Math.random() * 10),
      target: Math.floor(Math.random() * 10),
    }));

    // Set up the graph layout
    const width = 400;
    const height = 300;
    const svg = graphContainer
      .append('svg')
      .attr('width', width)
      .attr('height', height);

    // Create the graph elements
    const linkElements = svg
      .selectAll('line')
      .data(links)
      .enter()
      .append('line')
      .attr('stroke', 'gray')
      .attr('stroke-width', 2);

    const nodeElements = svg
      .selectAll('circle')
      .data(nodes)
      .enter()
      .append('circle')
      .attr('r', 10);

    console.log("nodeElements", nodeElements)
  }


  ngOnInit(): void {
    // load drag and drop component
    const dragAndDropComponent = new DragAndDropComponent();
    dragAndDropComponent.onDrop(new DragEvent("drop"));

    // wait for image is uploaded, generate graph


  }
}

