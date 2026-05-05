---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security"]
speakers: ["Yangmin Zhu", "Matt Mathew", "Uber"]
sched_url: https://kccncna2025.sched.com/event/27FdO/authenticating-and-authorizing-every-connection-at-uber-yangmin-zhu-matt-mathew-uber
youtube_search_url: https://www.youtube.com/results?search_query=Authenticating+and+Authorizing+Every+Connection+at+Uber+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Authenticating and Authorizing Every Connection at Uber - Yangmin Zhu & Matt Mathew, Uber

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Atlanta
- Speakers: Yangmin Zhu, Matt Mathew, Uber
- Schedule: https://kccncna2025.sched.com/event/27FdO/authenticating-and-authorizing-every-connection-at-uber-yangmin-zhu-matt-mathew-uber
- Busca YouTube: https://www.youtube.com/results?search_query=Authenticating+and+Authorizing+Every+Connection+at+Uber+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Authenticating and Authorizing Every Connection at Uber.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FdO/authenticating-and-authorizing-every-connection-at-uber-yangmin-zhu-matt-mathew-uber
- YouTube search: https://www.youtube.com/results?search_query=Authenticating+and+Authorizing+Every+Connection+at+Uber+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GYVNg0_FpwQ
- YouTube title: Authenticating and Authorizing Every Connection at Uber - Yangmin Zhu & Matt Mathew, Uber
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/authenticating-and-authorizing-every-connection-at-uber/GYVNg0_FpwQ.txt
- Transcript chars: 30102
- Keywords: policy, authorization, connection, actually, around, solution, change, traffic, caller, policies, library, envoy, metric, security, container, source, within, systems

### Resumo baseado na transcript

Um, we are here to discuss how we are authenticating and authorizing every connection at Uber. uh we'll talk about how we spent the last two three years uh building a service mesh which led us to actually authenticate and authorize every connection. So among this large tech stack, we have several security and compliance requirements that we need to meet and in order to do that we have to authenticate and authorize every single service call within Uber. So this is a solution that we built back in 2020 and you might think that this will work but in fact we ran into several problems there. Since the library is within these services whenever we have to do a fix like a security fix or even a bug fix now you had to go chase these 6,000 engineers again to go ahead and update the library within their system. Uh this solution is based on envoy and it is heavily inspired by architecture.

### Excerpt da transcript

Hello everyone, good afternoon. Um, we are here to discuss how we are authenticating and authorizing every connection at Uber. A quick intro about us. U, my name is Matt and I have young men here with me. We are from Uber. We represent engineering security within Uber. uh we'll talk about how we spent the last two three years uh building a service mesh which led us to actually authenticate and authorize every connection. A quick overview of the agenda. We'll start with uh the goal of why we are doing this. Uh we'll talk about the solution that we implemented, some of the things that we did to improve the adoption of the solution. We'll talk about some of the key lessons that we learned and then finally end with some of our takeaways. Before we jump into why are we doing this, I do want to set some context on Uber's landscape. Uh we have a pretty large tech stack that we operate at Uber. Back in 2015, Uber adopted a microser based architecture. So in the last 10 years or so, uh we have built over 7,000 microservices.

We are operating around 7,000 databases. Um and also almost half a million data jobs. In addition to that, we leverage multiple RPC frameworks. We utilize around five languages or so. And last but not the least, we're not 100% on Kubernetes yet. We have several container orchestration systems. Some of them are open source, some of them are also built in-house. So what you can see here is we operate at large scale highly heterogeneous land system. And um one of the thing key things to notice over here is that we are also leveraging several open source technologies. Keep this in mind because this is going to influence the solution. So among this large tech stack, we have several security and compliance requirements that we need to meet and in order to do that we have to authenticate and authorize every single service call within Uber. So this is our goal right back around uh 2020 or so or 2019 2020 roughly five or six years ago we actually started building a solution which is completely library based and what this library does is we ask all the service owners at Uber to go ahead and adopt this library.

So if a service A is calling service B then the on the caller side this library goes ahead and works with spire gets a X19 certificate from spire follows Py standard utilizes that to create something called a jot token nothing fancy there J token is utilized to perform the authentication on the caller side on the call E side on service B the toke
