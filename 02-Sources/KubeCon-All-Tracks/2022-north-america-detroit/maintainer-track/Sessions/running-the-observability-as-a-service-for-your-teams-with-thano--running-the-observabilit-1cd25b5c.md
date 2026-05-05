---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Ben Ye", "Amazon Web Services", "Bartłomiej Płotka", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182NL/running-the-observability-as-a-service-for-your-teams-with-thanos-ben-ye-amazon-web-services-bartlomiej-plotka-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Running+the+Observability+As+a+Service+For+Your+Teams+With+Thanos+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Running the Observability As a Service For Your Teams With Thanos - Ben Ye, Amazon Web Services & Bartłomiej Płotka, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Ben Ye, Amazon Web Services, Bartłomiej Płotka, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182NL/running-the-observability-as-a-service-for-your-teams-with-thanos-ben-ye-amazon-web-services-bartlomiej-plotka-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Running+the+Observability+As+a+Service+For+Your+Teams+With+Thanos+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Running the Observability As a Service For Your Teams With Thanos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182NL/running-the-observability-as-a-service-for-your-teams-with-thanos-ben-ye-amazon-web-services-bartlomiej-plotka-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Running+the+Observability+As+a+Service+For+Your+Teams+With+Thanos+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=I4Mfyfd_4M8
- YouTube title: Running the Observability As a Service For Your Teams With Thanos - Ben Ye & Bartłomiej Płotka
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/running-the-observability-as-a-service-for-your-teams-with-thanos/I4Mfyfd_4M8.txt
- Transcript chars: 32242
- Keywords: series, storage, engine, premisus, promql, thanos, already, essentially, actually, queries, multiple, receiver, certain, memory, observability, called, another, solution

### Resumo baseado na transcript

thank you okay I can hear my mic is should work so welcome everyone um Welcome to our tanos introduction slash some Trends some SL SL some updates and live demo presentation we are super excited to be here and and really yeah meet all the people like sometimes in person like I I met Ben in person for the first time as well even though we were working for like two years almost in the community so it's amazing to be to be in person here so welcome um

### Excerpt da transcript

thank you okay I can hear my mic is should work so welcome everyone um Welcome to our tanos introduction slash some Trends some SL SL some updates and live demo presentation we are super excited to be here and and really yeah meet all the people like sometimes in person like I I met Ben in person for the first time as well even though we were working for like two years almost in the community so it's amazing to be to be in person here so welcome um so I have Ben with me today and so thank you BK so this is Ben year and uh I'm a software development engineer at AWS and I'm one of the maintainer of the Sonos project and I'm also contributors to some cncf projects like cortex premisus ago CD Etc and I have a papy called GUI thank you yeah my name is uh B PKA you can call me BK I principal software engineer at Red Hat I maintainer of various projects including promus and tanos lots of go line projects as well and uh I'm active in the cncf I also recently have my puppy is purple Heron because I wrote a book uh it's finished is being published in November so pretty soon you can pre-order it now it's efficient go uh about you know how to write efficient goang but really it's also language agnostic how to have a good observability driven practices over towards better efficiency of your Solutions um but yeah let's really start with just introducing tanos um maybe you know what tanos is maybe not um maybe yeah let's ask like how please raise a hand if you know what what tannos project is well actually amazing yeah so maybe it will be just um reiteration or maybe you will learn something new so I will let Ben to to introduce tanos right now thanks spk so to introduce tanos uh let's start with the story of uh premisus first premisus is a monitoring system that is mainly inspired by Google bormon so with premisus we are providing a highly reliable easy to operate monitoring solution and it's just a single binary but it provides very uh many powerful features like data scraping querying using very flexible promql and alerting and uh but premisus comes with its own problem because uh it somewhat lacks scalability and high availability and here this brings us to Thanos which is a distributed premisus and Thanos is more High scalable and horizontally um premisus it provides a global view for querying multiple premisus at the same time instead of using a local disk as premisus it uses object storage like S3 to store long-term data and it also offers some other features like
