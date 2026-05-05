---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["Community Governance"]
speakers: ["Marc Duiker", "Community Manager"]
sched_url: https://kccncna2025.sched.com/event/27d5j/project-lightning-talk-dapr-start-building-distributed-applications-with-ease-using-building-block-apis-marc-duiker-community-manager
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Dapr%3A+Start+Building+Distributed+Applications+With+Ease+Using+Building+Block+APIs+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Dapr: Start Building Distributed Applications With Ease Using Building Block APIs - Marc Duiker, Community Manager

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Marc Duiker, Community Manager
- Schedule: https://kccncna2025.sched.com/event/27d5j/project-lightning-talk-dapr-start-building-distributed-applications-with-ease-using-building-block-apis-marc-duiker-community-manager
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Dapr%3A+Start+Building+Distributed+Applications+With+Ease+Using+Building+Block+APIs+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Dapr: Start Building Distributed Applications With Ease Using Building Block APIs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5j/project-lightning-talk-dapr-start-building-distributed-applications-with-ease-using-building-block-apis-marc-duiker-community-manager
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Dapr%3A+Start+Building+Distributed+Applications+With+Ease+Using+Building+Block+APIs+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N7ocoqSUNV4
- YouTube title: Project Lightning Talk: Dapr: Start Building Distributed Applications With Ease Using... Marc Duiker
- Match score: 0.959
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-dapr-start-building-distributed-applications-wi/N7ocoqSUNV4.txt
- Transcript chars: 4958
- Keywords: workflow, application, certain, dapper, actually, workflows, distributed, agentic, systems, sidecar, support, applications, around, offers, reliable, microservices, organizations, development

### Resumo baseado na transcript

Uh, I'm Mark Derer, one of the Deer community managers, and I'm here to talk about building distributed applications with ease using building block APIs. I mean, I had to give the birds some hats here as I'm wearing a Dapper hat as well. So it really makes your application and your whole architecture like more flexible and more portable. Um also the yeah workflow improvement has been um performance has been improved a lot.

### Excerpt da transcript

Hi everyone. Uh, I'm Mark Derer, one of the Deer community managers, and I'm here to talk about building distributed applications with ease using building block APIs. And this is all about the Deer project. I mean, I had to give the birds some hats here as I'm wearing a Dapper hat as well. Uh, so Deer stands for the distributed application runtime. It's a graduated CNCF project since last November. It's been around for about six years. And um, yeah, it offers APIs for building secure and reliable microservices and agentic AI systems. I mean, we all have to jump on board of the AI stuff a bit anyway, right? So, it's used by a lot of big organizations and each year we do like a a survey across Deer developers and on average they claim to save 30% of development time for when they use Deer versus not using Dapper. So, it's really a big time saver uh for your development teams if they use Dapper to to build their microser backends. So uh Deer runs as a sidecar next to your application and the sidecar offers a lot of uh APIs that uh that you can use from your application.

Uh and the really cool thing about Dapper is that it decouples your application uh layer from the underlying infrastructure. So as an example uh Dapper has a popsup API to do like asynchronous messaging but Deer itself is not a message broker but you can configure Deer with GML files to use like many different message brokers out there. And the same is goes for secrets and state management and and so on. So it really makes your application and your whole architecture like more flexible and more portable. All right. Um just some highlights of a very recent u deer API. So one of the very big ones which has a lot of interest is called deer workflow. So now the deer sidecar has like a built-in workflow engine. Uh it's based on the durable execution concept which saves the workflow state to a deer compatible state store. So even in case your application fails completely maybe a whole node goes down when that node comes back up the deer will actually recognize that some workflows were still like in flight and haven't been completed and deer actually make sure that that workflow will actually uh run to completion.

Um, deer workflow integrates like seamlessly with all of the other deer APIs which is great and you author your workflows in code. So you can use like C or Java or Python or Go or JavaScript to write your workflows and your activities. Um, you can also apply lots of workflow specific patt
