---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/monitoring-in-store-point-of-sal/
youtube_url: https://www.youtube.com/watch?v=0a8dzLEow3Q
youtube_search_url: https://www.youtube.com/results?search_query=Monitoring+In-Store+Point+of+Sales+Infrastructure+with+Prometheus+and+Netbox+PromCon+2022
video_match_score: 1.035
status: video-found
---

# Monitoring In-Store Point of Sales Infrastructure with Prometheus and Netbox

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/monitoring-in-store-point-of-sal/
- YouTube: https://www.youtube.com/watch?v=0a8dzLEow3Q

## Resumo

Speaker(s): Felix Peters Monitoring bare metal infrastructure with Prometheus is hard because there is no easy way for service discovery. We had the challenge of monitoring our new point of sales infrastructure in stores which contains cash desk hardware, printers and card payment terminals. These devices should be auto discoverable without the pain of static service discovery.

## Abstract oficial

Speaker(s): Felix Peters

Monitoring bare metal infrastructure with Prometheus is hard because there is no easy way for service discovery. We had the challenge of monitoring our new point of sales infrastructure in stores which contains cash desk hardware, printers and card payment terminals. These devices should be auto discoverable without the pain of static service discovery. Prometheus was already the monitoring solution we love and have experience with. 

This talk is about how we solved this challenge by using Netbox as an inventory management system, integrated with Prometheus using the new http service discovery method. We will discuss several solutions, strategies, pitfalls and how this could be scaled to any kind of classic infrastructure.
It's also about how this increased the quality of our infrastructure documentation, just because engineers get a real benefit of writing down what's deployed while getting monitoring just out of the box.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/monitoring-in-store-point-of-sal/
- YouTube: https://www.youtube.com/watch?v=0a8dzLEow3Q
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0a8dzLEow3Q
- YouTube title: PromCon EU 2022: Monitoring In-Store Point of Sales Infrastructure with Prometheus and Netbox
- Match score: 1.035
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/monitoring-in-store-point-of-sales-infrastructure-with-prometheus-and/0a8dzLEow3Q.txt
- Transcript chars: 18892
- Keywords: netbox, devices, prometheus, inventory, native, monitor, windows, device, monitoring, instance, active, infrastructure, running, server, source, metrics, moment, central

### Resumo baseado na transcript

[Music] foreign [Music] yes wonderful um thanks for introduction um first of all thanks for the organization here um to have us here back in person it's great and it's a pleasure to be attending on Saturday night's conference so a real big thank to all of you guys making this happen we want to talk about monitoring Point of Sales infrastructure so this is more a non-technical talk it's not hardcore technical like we had it this morning but it's about what we can achieve with promo charge and

### Excerpt da transcript

[Music] foreign [Music] yes wonderful um thanks for introduction um first of all thanks for the organization here um to have us here back in person it's great and it's a pleasure to be attending on Saturday night's conference so a real big thank to all of you guys making this happen we want to talk about monitoring Point of Sales infrastructure so this is more a non-technical talk it's not hardcore technical like we had it this morning but it's about what we can achieve with promo charge and in a way which is not really cloud native so um a short reminder um my name is Felix I'm engineering lead at operations core tooling team at broningham my team is responsible for running core infrastructure and Linux Based Services so we we do many things with Prometheus and Cloud native stuff but also help other teams which we will talk today so yeah Point of Sales this is everything which is located in a physical store so cash desk stuff like that everything we need to yeah make money um oh where it's my starting point yeah so yeah that's our starting point for for this talk um proninger is a luxury fashion store retailer mostly here in such Germany we are running multiple stores Outlets uh yeah where we have luxury fashion stuff like that um of course we have cache desks and in 2020 we had a challenge that there will be a new Point of Sales system which was introduced or announced by yeah some Architects the old one was pretty long in service and it had just pink checks with knowledge monitoring tool called prtg maybe you know it and yeah my team was called to support the the technicals of these Point of Sales and structure to support them um in running this system so yeah we already had Prometheus and we loved it so it was our Natural Choice to use it and yeah there are some issues we had to solve to make this happen so um on the first run here are the overview house search upon the state system uh oxidated uh only of course we have parameters as our monitoring solution and on the job we have the core Linux Based Services they are responsible for handling all the the registrations all the the processes so it's uh the cloud database it's a cloud instance or multiple Cloud instance in one of the major public clouds so it wasn't big to issue we we know how to monitor this stuff because here the exporters they are Services Curry everything is nice the more challenging part is about how can we monitor the devices in our stores and these stores are built in a layered sys
