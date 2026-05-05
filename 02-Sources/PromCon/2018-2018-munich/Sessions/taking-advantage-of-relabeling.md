---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/taking-advantage-of-relabeling/
youtube_url: https://www.youtube.com/watch?v=QufG6rjbsOM
youtube_search_url: https://www.youtube.com/results?search_query=Taking+Advantage+of+Relabeling+PromCon+2018
video_match_score: 0.952
status: video-found
---

# Taking Advantage of Relabeling

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/taking-advantage-of-relabeling/
- YouTube: https://www.youtube.com/watch?v=QufG6rjbsOM

## Resumo

Speaker: Julien Pivotto Relabeling is a powerful feature of Prometheus but it is also quite specific to the project. This talk will explain and demonstrate relabeling, with some real use cases. After the presentation, you will understand relabeling and stop to copy/paste relabeling rules you don't understand.

## Abstract oficial

Speaker: Julien Pivotto

Relabeling is a powerful feature of Prometheus but it is also quite specific to the project. This talk will explain and demonstrate relabeling, with some real use cases. After the presentation, you will understand relabeling and stop to copy/paste relabeling rules you don't understand.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/taking-advantage-of-relabeling/
- YouTube: https://www.youtube.com/watch?v=QufG6rjbsOM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QufG6rjbsOM
- YouTube title: PromCon 2018: Taking Advantage of Relabeling
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/taking-advantage-of-relabeling/QufG6rjbsOM.txt
- Transcript chars: 17988
- Keywords: matrix, labels, configuration, metric, primitives, change, target, exporter, server, address, actually, metrics, primitive, remote, traffic, dropping, instance, scrape

### Resumo baseado na transcript

[Applause] so I come from Belgium and my main interests are about automation my drivability I'm contributing to primitives to grow fauna and I am also I've also started the graph unit project so to create a graph and a dashboard using JSON it so I work for in which we have a European company we do open source consultancy across different kinds of organizations but now let's talk about labels so let's first get back to the basics like what symmetric in primitives well it's a name and then

### Excerpt da transcript

[Applause] so I come from Belgium and my main interests are about automation my drivability I'm contributing to primitives to grow fauna and I am also I've also started the graph unit project so to create a graph and a dashboard using JSON it so I work for in which we have a European company we do open source consultancy across different kinds of organizations but now let's talk about labels so let's first get back to the basics like what symmetric in primitives well it's a name and then it's a key value pairs so that you have like the name of the matrix in this case it's like it's a proxy HTTP response is todo and then you have a catenary T which is all the different stuff that are attached to that like the back end is squid call this 1 X X environment is acceptance for example so all of that makes what we call a metric what you might not know is that a metric name is also a label like it is the label underscore underscore name is conozco so that's also a label so you can everywhere where you use a label you can actually alter the name change the name and you can do some stuff like that like you want to understand when the cadet is coming from then you can count your metrics by name so that you have the count value which usually removes the name of the metrics but you can explicitly say okay please keep the name so that I know which metrics after I ask add an ID for example primitives itself also add some labels when it scrapes metrics like it will add a job and an instance label you can add static labels also in the job configuration so that you also evolve EDF you always have basically labels attached to your metrics well you should at least so but labels is more than that so promoted is using them all over the place so it start in the configuration so when primitives is doing the configuration and it's looking hey what should i scrape now it will also have some labels to say okay this is my configuration this is my target so this is also using labels when it will fetch the targets it will fetch the labels that have exposed by the target but also at throne override one of the target and after it has done that it can also like alter the labels labelling and when you also record holes it will do the same it will use labels and it will enables you to add labels with your high cutting holes also in the Federation so when you have a printing service that's Federation other one it will get the external labels on top of the primitive levels and when it send al
