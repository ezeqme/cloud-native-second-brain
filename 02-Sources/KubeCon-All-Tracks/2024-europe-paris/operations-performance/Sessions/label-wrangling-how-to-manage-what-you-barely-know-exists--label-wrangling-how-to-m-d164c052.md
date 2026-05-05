---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Jeremy Mechouche", "Carl Castanier", "Devoteam"]
sched_url: https://kccnceu2024.sched.com/event/1YeSU/label-wrangling-how-to-manage-what-you-barely-know-exists-jeremy-mechouche-carl-castanier-devoteam
youtube_search_url: https://www.youtube.com/results?search_query=Label+Wrangling%3A+How+to+Manage+What+You+Barely+Know+Exists%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Label Wrangling: How to Manage What You Barely Know Exists! - Jeremy Mechouche & Carl Castanier, Devoteam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Jeremy Mechouche, Carl Castanier, Devoteam
- Schedule: https://kccnceu2024.sched.com/event/1YeSU/label-wrangling-how-to-manage-what-you-barely-know-exists-jeremy-mechouche-carl-castanier-devoteam
- Busca YouTube: https://www.youtube.com/results?search_query=Label+Wrangling%3A+How+to+Manage+What+You+Barely+Know+Exists%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Label Wrangling: How to Manage What You Barely Know Exists!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSU/label-wrangling-how-to-manage-what-you-barely-know-exists-jeremy-mechouche-carl-castanier-devoteam
- YouTube search: https://www.youtube.com/results?search_query=Label+Wrangling%3A+How+to+Manage+What+You+Barely+Know+Exists%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DiFRXehykxI
- YouTube title: Label Wrangling: How to Manage What You Barely Know Exists! - Jeremy Mechouche & Carl Castanier
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/label-wrangling-how-to-manage-what-you-barely-know-exists/DiFRXehykxI.txt
- Transcript chars: 17527
- Keywords: resources, resource, environment, knowledge, basically, context, application, present, labeling, access, define, consider, question, manage, several, information, native, security

### Resumo baseado na transcript

okay so it's 4: so we could start uh so thank you everybody for joining us today so we are going to present you um how talks are label wrangling so how to manage what you barely know exist um uh my name is Jeremy Mish so I'm a research Innovation project manager at Devo team uh I'm presenting today with uh Carl C which is a cloud devops architect so this work and this presentation is based on a project we aim we um we work on uh at

### Excerpt da transcript

okay so it's 4: so we could start uh so thank you everybody for joining us today so we are going to present you um how talks are label wrangling so how to manage what you barely know exist um uh my name is Jeremy Mish so I'm a research Innovation project manager at Devo team uh I'm presenting today with uh Carl C which is a cloud devops architect so this work and this presentation is based on a project we aim we um we work on uh at research and Innovation section of Devo team so we are working on the research ACC access on autonomous Cloud uh and the subject of label is uh key to allow us to constru construct this autonomous Cloud so that's why we work on label uh and we present today this work so okay so let's start the Wrangle so the this presentation is decomposed in five uh steps so the first one will be uh to uh Define what is a label uh what is not a label so it's the main key for cloud native environment is labels uh then uh Carl will present you the common use case uh based on label and what happen when you uh when you forget to consider labeling and then I will take take back and present you the labeling best practices and the Wrangle for homogeneity so what is a label so a label is basically a key value pair uh which is as which is Define which is um tag on resources a resources has a name and Technical characteristics and the label will allow to uh add functional context to it so to for an example we'll get we'll take a pod because we talk about kubernetes here um this pod is a um is tagged is labeled with environment Dev and project dvo1 so which say that this resources is belong to the project d one and the development environment um what we want also to say on the label that uh they are not hierarchical um they're flat and transversal so you can use label on any kind of resources in cloud computing context but any other context you can you can think of um and that's the topics so what is not a label so we consider two uh set of uh properties for resource so the first one which is not labeled uh are the intrinsic properties so basically the kind the image the version the request and limits so still in a pod context in a pod example uh and then which is labels will be the extrange properties so now we can see project system version environment we consider that as label um so basically it's as I said anything that can have functional context to um the resource but just for conclude the slide uh labels does not produce anything it allow to identi
