---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Andrea Frittoli", "IBM"]
sched_url: https://kccncna2021.sched.com/event/lV1H/sig-events-using-cloudevents-to-create-an-interoperable-cicd-ecosystem-andrea-frittoli-ibm
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Events%3A+Using+CloudEvents+to+Create+an+Interoperable+CI%2FCD+Ecosystem+CNCF+KubeCon+2021
slides: []
status: parsed
---

# SIG Events: Using CloudEvents to Create an Interoperable CI/CD Ecosystem - Andrea Frittoli, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: United States / Los Angeles
- Speakers: Andrea Frittoli, IBM
- Schedule: https://kccncna2021.sched.com/event/lV1H/sig-events-using-cloudevents-to-create-an-interoperable-cicd-ecosystem-andrea-frittoli-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Events%3A+Using+CloudEvents+to+Create+an+Interoperable+CI%2FCD+Ecosystem+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre SIG Events: Using CloudEvents to Create an Interoperable CI/CD Ecosystem.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1H/sig-events-using-cloudevents-to-create-an-interoperable-cicd-ecosystem-andrea-frittoli-ibm
- YouTube search: https://www.youtube.com/results?search_query=SIG+Events%3A+Using+CloudEvents+to+Create+an+Interoperable+CI%2FCD+Ecosystem+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iPD8dtsEUSk
- YouTube title: SIG Events: Using CloudEvents to Create an Interoperable CI/CD Ecosystem - Andrea Frittoli, IBM
- Match score: 0.957
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sig-events-using-cloudevents-to-create-an-interoperable-ci-cd-ecosyste/iPD8dtsEUSk.txt
- Transcript chars: 18758
- Keywords: events, captain, pipeline, deployment, tecton, create, artifact, together, application, version, integration, vocabulary, format, player, sequence, results, pipelines, common

### Resumo baseado na transcript

hello welcome to seek events using cloud events to create an interoperable ci cd before we dive in let me introduce myself my name is andrea fritoli i work as a software engineer and developer advocate at ibm my focus is on open source and devops technologies i'm a member of the technical oversight committee at the continuous delivery foundation i'm also the co-chair of the event special interest group as well as a maintainer of the tectum project this presentation is the result of the work that we did

### Excerpt da transcript

hello welcome to seek events using cloud events to create an interoperable ci cd before we dive in let me introduce myself my name is andrea fritoli i work as a software engineer and developer advocate at ibm my focus is on open source and devops technologies i'm a member of the technical oversight committee at the continuous delivery foundation i'm also the co-chair of the event special interest group as well as a maintainer of the tectum project this presentation is the result of the work that we did together with mauricio salatino unfortunately it was not possible for both of us to present together so here i am i'd like to start today with a little story so two devops engineers meet in the corridor of kubecon and cloudnativecon north america they've both been working on setting up their cd pipelines for their respective teams and they are now sharing ideas and experiences the first one i've been working with tacton his team is really happy about how quickly they could set up build and deployment pipelines using existing building blocks the second one i've been working with captain her team had a positive experience with quality weights gates and remediation flows now they are thinking that they don't really want to choose they'd like the best of the two words oh and they would have to integrate the pipelines from the security teams as well that run on jenkins infrastructure so is that possible how many point-to-point integration will they need one way to integrate the different platforms might be through events that way they'd achieve a decoupled scalable and fault tolerant integration some of the platforms already speak cloud events however the issue is that even with cloud events there are no consistent abstractions or share semantics between the different projects and this is right the kind of issues that the cdf wants to help solving so cdf stands for continuous delivery foundation and that is a place where all the projects related to delivering application and software can gather shared ideas and collaborate the ci cd landscape keeps growing and there is a real need for best practices examples showing how to use multiple tools together and documenting what each project is about the cd foundation is home for jenkins jenkins tecton spinach among others that are in the incubation stage if you want to collaborate and join the foundation visit the cdf site and get in touch so maybe we can use events um but we need some kind of standardization inside the
