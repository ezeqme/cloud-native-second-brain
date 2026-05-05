---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Observability", "Security"]
speakers: ["Ron Vider", "Oxeye"]
sched_url: https://kccnceu2023.sched.com/event/1HyYT/using-opentelemetry-for-application-security-with-a-real-life-example-ron-vider-oxeye
youtube_search_url: https://www.youtube.com/results?search_query=Using+OpenTelemetry+for+Application+Security%2C+with+a+Real+Life+Example+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Using OpenTelemetry for Application Security, with a Real Life Example - Ron Vider, Oxeye

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Observability]], [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ron Vider, Oxeye
- Schedule: https://kccnceu2023.sched.com/event/1HyYT/using-opentelemetry-for-application-security-with-a-real-life-example-ron-vider-oxeye
- Busca YouTube: https://www.youtube.com/results?search_query=Using+OpenTelemetry+for+Application+Security%2C+with+a+Real+Life+Example+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Using OpenTelemetry for Application Security, with a Real Life Example.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYT/using-opentelemetry-for-application-security-with-a-real-life-example-ron-vider-oxeye
- YouTube search: https://www.youtube.com/results?search_query=Using+OpenTelemetry+for+Application+Security%2C+with+a+Real+Life+Example+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hz3ncpPKzUs
- YouTube title: Using OpenTelemetry for Application Security, with a Real Life Example - Ron Vider, Oxeye
- Match score: 0.976
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/using-opentelemetry-for-application-security-with-a-real-life-example/hz3ncpPKzUs.txt
- Transcript chars: 23517
- Keywords: vulnerabilities, vulnerability, understand, security, internal, application, external, native, message, microservices, function, internet, information, applications, observability, architecture, hacker, request

### Resumo baseado na transcript

welcome to my talk using open Telemetry for application security purposes in this presentation we will discuss the evolution of application security and code vulnerabilities I would shift to Cloud native affected code vulnerabilities we will see some examples and the way we used open Telemetry in order to solve these problems that happen because of the shift to Cloud native we have only 35 minutes so let's jump into the details I'll start with a short introduction about myself so my name is ronvita I'm the co-founder and CTO one contained only one micro service now I will send another request to the API that will trigger cross service communication so this time I will send a command to slash internal with a query param called data and I can send the hello and

### Excerpt da transcript

welcome to my talk using open Telemetry for application security purposes in this presentation we will discuss the evolution of application security and code vulnerabilities I would shift to Cloud native affected code vulnerabilities we will see some examples and the way we used open Telemetry in order to solve these problems that happen because of the shift to Cloud native we have only 35 minutes so let's jump into the details I'll start with a short introduction about myself so my name is ronvita I'm the co-founder and CTO of oxide security in oxide we are building a application security platform for cloud native environment so we are helping organization to find vulnerabilities in their custom calls for kubernetes based applications I've been around in cyber security landscape for over a decade since I learned how to hack websites when I was 16 years old built my sales application security testing tools and in my free time I like to look for new vulnerabilities and do security research and in the past few years I'm highly focused on the cloud native landscape so a short overview of the agenda for this presentation and like I said earlier we'll start with reviewing the evolution of application vulnerabilities or code vulnerabilities vulnerability in the code that is written within the organization we will see some example of vulnerability that we found in Cloud native project and since you have project actually we will do a short introduction about what is open Telemetry and observability why do we need observability in order to understand our applications and then we will be able to talk of about how we can connect these two things together application security and observability with open telemetry and finally we'll be able to see a live demo of a project a cloud native vulnerable lab with open Telemetry installed and how it helps us to understand code vulnerabilities much better so let's start um we'll start with reviewing what happened to code vulnerabilities in the in the past few years because if we look on the shift that happened to Applications 15 years ago when we developed application we used monolithic architecture it all was a big chunk of code deployed on a server somewhere in the internet but today applications are distributed they are built in microservices architecture you know so we went from local Development building monolithic application into distributed application and this CH this change in the architecture also affected the way vul
