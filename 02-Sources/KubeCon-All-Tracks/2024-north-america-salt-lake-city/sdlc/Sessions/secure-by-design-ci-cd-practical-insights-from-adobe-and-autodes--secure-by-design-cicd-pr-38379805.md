---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "SDLC"
themes: ["Security"]
speakers: ["Vikram Sethi", "Adobe Inc.", "Jesse Sanford", "Autodesk"]
sched_url: https://kccncna2024.sched.com/event/1i7lS/secure-by-design-cicd-practical-insights-from-adobe-and-autodesk-vikram-sethi-adobe-inc-jesse-sanford-autodesk
youtube_search_url: https://www.youtube.com/results?search_query=Secure+by+Design+CI%2FCD%3A+Practical+Insights+from+Adobe+and+Autodesk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Secure by Design CI/CD: Practical Insights from Adobe and Autodesk - Vikram Sethi, Adobe Inc. & Jesse Sanford, Autodesk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[SDLC]]
- Temas: [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Vikram Sethi, Adobe Inc., Jesse Sanford, Autodesk
- Schedule: https://kccncna2024.sched.com/event/1i7lS/secure-by-design-cicd-practical-insights-from-adobe-and-autodesk-vikram-sethi-adobe-inc-jesse-sanford-autodesk
- Busca YouTube: https://www.youtube.com/results?search_query=Secure+by+Design+CI%2FCD%3A+Practical+Insights+from+Adobe+and+Autodesk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Secure by Design CI/CD: Practical Insights from Adobe and Autodesk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lS/secure-by-design-cicd-practical-insights-from-adobe-and-autodesk-vikram-sethi-adobe-inc-jesse-sanford-autodesk
- YouTube search: https://www.youtube.com/results?search_query=Secure+by+Design+CI%2FCD%3A+Practical+Insights+from+Adobe+and+Autodesk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gIkCVKTnCZw
- YouTube title: Secure by Design CI/CD: Practical Insights from Adobe and Autodesk - Vikram Sethi & Jesse Sanford
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/secure-by-design-ci-cd-practical-insights-from-adobe-and-autodesk/gIkCVKTnCZw.txt
- Transcript chars: 42555
- Keywords: artifact, actually, pipeline, reference, security, platform, attestation, little, architecture, evidence, command, software, deploy, developer, change, witness, finally, separate

### Resumo baseado na transcript

talk a little bit about sof Supply in security how we think about it dig deeper into the reference architecture and talk a little bit about the sglc at each of our organizations uh and wrap it up with a demo and some learnings and takeaways so um before we get started you know some questions that we really ask ourselves as we are uh securing our CD pipelines these are the questions that we ask internally ourselves so it's good to you know get a sense of how you're

### Excerpt da transcript

talk a little bit about sof Supply in security how we think about it dig deeper into the reference architecture and talk a little bit about the sglc at each of our organizations uh and wrap it up with a demo and some learnings and takeaways so um before we get started you know some questions that we really ask ourselves as we are uh securing our CD pipelines these are the questions that we ask internally ourselves so it's good to you know get a sense of how you're thinking about these first question how do you know if the code that you're building or the artifact that you're deploying has not been exploited would do you even get to know second can your developers bypass security controls in their cicd pipelines as in if you're providing a cicd pipeline to them can they take out uh scanning uh out of the equation or delete that particular step for example the third one how do you determine the blast radius and cost of an exploited dependency we have measures in place or instrumentation in place to be able to do that so how many of you show hands how many of you are able to relate to these questions or think that these are relevant questions to ask as you're building the CD pipelines great thank you so much so as we think about software supply chain security we believe that it's more than cicd of course but it starts with the onboarding a lot of organizations and Enterprises in particular we provide onboarding capab abilities to developers so we provide those templates so we start with the templates or the onboarding uh capabilities and go till the post deployments and the operations and everything in between all of that needs to be secure and um when we think about security or software supply chain security we need to also think about processes workflows and also people a lot of the time the organizations they are too focused on architecture and design and they forget about the processes and the people part which are equally important and when you think about like you know the architecture in particular you would want to you normally have a layered kind of an architecture so you would have infrastructure at the bottom and developer services at the top where the developers are interacting with the system so you need to you know secure all these layers you know from the infrastructure right to the developer surfaces and what do you get in return you get Integrity authenticity and non- reputation so with that that uh let's uh go to the reference architecture b
