---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security", "Storage Data", "Runtime Containers"]
speakers: ["Aurélien Bombo", "Microsoft"]
sched_url: https://kccnceu2025.sched.com/event/1txCP/trust-no-one-secure-storage-with-confidential-containers-aurelien-bombo-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Trust+No+One%3A+Secure+Storage+With+Confidential+Containers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Trust No One: Secure Storage With Confidential Containers - Aurélien Bombo, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Aurélien Bombo, Microsoft
- Schedule: https://kccnceu2025.sched.com/event/1txCP/trust-no-one-secure-storage-with-confidential-containers-aurelien-bombo-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Trust+No+One%3A+Secure+Storage+With+Confidential+Containers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Trust No One: Secure Storage With Confidential Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txCP/trust-no-one-secure-storage-with-confidential-containers-aurelien-bombo-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Trust+No+One%3A+Secure+Storage+With+Confidential+Containers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=etCmLttqJsQ
- YouTube title: Trust No One: Secure Storage With Confidential Containers - Aurélien Bombo, Microsoft
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/trust-no-one-secure-storage-with-confidential-containers/etCmLttqJsQ.txt
- Transcript chars: 25840
- Keywords: container, storage, policy, confidential, device, containers, security, create, inside, driver, encryption, components, called, trusted, cluster, addestation, addition, deploy

### Resumo baseado na transcript

Uh not my first time in London though because I'm born and raised in Belgium, so not too far from here. Um I work with the confidential containers project where I help out with different aspects around the project notably the CI and then you know lately I've been looking at storage. And so with this, I'll talk about both the implementation itself, but also how that ties into the broader ecosystem so that we can deploy this at scale, right? So the way that this presentation is going to unfold is that uh first I'm going to give some context on you know container runtimes confidential computing and how that works with Kubernetes and then I'll split the presentation into two parts. first the firmal storage and then we're going to build on top of that uh to detail a bit persistent storage right and then in between that I have a demo based on the existing code right based on that PR that I was uh mentioning a minute ago. security this is we don't say that you know we said this is not secure at all right because uh you're essentially one kernel vulnerability away from having a container breakout where one of your containers uh you know escapes the this uh this namespace

### Excerpt da transcript

All right, let's do this. Hi everyone. How you guys doing? My name is Aurelian Bombo. I'm very happy to be here. Very excited. This is my first Yukon. I made the trip all the way from Chicago. Uh not my first time in London though because I'm born and raised in Belgium, so not too far from here. Um you know, pretty familiar with London. Kind of. Definitely not familiar with sunny London. So that's amazing. Um I work with the confidential containers project where I help out with different aspects around the project notably the CI and then you know lately I've been looking at storage. I also work with the Kata containers project where I serve on the architecture committee there which is a group that uh you know sears a project and has a final sale on decisions and then at Microsoft my assignment really is the Linux confidential platform as part of the Azure Linux OS team and so in the confidential containers project we believe that confidential computing is the future of computing right? Uh where people want to protect data not only you know at rest and in transit but also in use right protect that data from their cloud provider.

So the thing is when we talk about confidential computing usually we uh focus a lot on the compute part right not so much on networking or storage right and so today I wanted to um you know share with you guys a little bit about what we've been working on with the confidential containers community uh and so you know to enable secure storage right and containers from a confidential standpoint and so Mind you, a lot of this stuff is still very much a work in progress, but at least this will give you a good overview on the current state of things, right? And so with this, I'll talk about both the implementation itself, but also how that ties into the broader ecosystem so that we can deploy this at scale, right? And so I also have a PR uh that I'm working on in the uh confidential containers repo to enable all this, right? And so I'll share it at the end of this presentation if you guys want to take a look at it, right? And uh judge my code maybe. So the way that this presentation is going to unfold is that uh first I'm going to give some context on you know container runtimes confidential computing and how that works with Kubernetes and then I'll split the presentation into two parts.

first the firmal storage and then we're going to build on top of that uh to detail a bit persistent storage right and then in between that I have a dem
