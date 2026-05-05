---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Alan Chung Ma", "Keytos", "Justin Cappos", "New York University"]
sched_url: https://kccnceu2025.sched.com/event/1tcyf/attesting-and-verifying-your-software-supply-chain-with-in-toto-alan-chung-ma-keytos-justin-cappos-new-york-university
youtube_search_url: https://www.youtube.com/results?search_query=Attesting+and+Verifying+Your+Software+Supply-Chain+With+In-toto+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Attesting and Verifying Your Software Supply-Chain With In-toto - Alan Chung Ma, Keytos & Justin Cappos, New York University

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Alan Chung Ma, Keytos, Justin Cappos, New York University
- Schedule: https://kccnceu2025.sched.com/event/1tcyf/attesting-and-verifying-your-software-supply-chain-with-in-toto-alan-chung-ma-keytos-justin-cappos-new-york-university
- Busca YouTube: https://www.youtube.com/results?search_query=Attesting+and+Verifying+Your+Software+Supply-Chain+With+In-toto+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Attesting and Verifying Your Software Supply-Chain With In-toto.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyf/attesting-and-verifying-your-software-supply-chain-with-in-toto-alan-chung-ma-keytos-justin-cappos-new-york-university
- YouTube search: https://www.youtube.com/results?search_query=Attesting+and+Verifying+Your+Software+Supply-Chain+With+In-toto+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Cydz0hadVuQ
- YouTube title: Attesting and Verifying Your Software Supply-Chain With In-toto - Alan Chung Ma & Justin Cappos
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/attesting-and-verifying-your-software-supply-chain-with-in-toto/Cydz0hadVuQ.txt
- Transcript chars: 29813
- Keywords: basically, supply, software, specific, compliance, actually, information, policy, source, certain, attestation, layout, compiler, version, within, attestations, stations, everyone

### Resumo baseado na transcript

I'm a software engineer at a small company and I'm a maintainer of Into. So we're going to be talking to you a bit about Intto and trying to give you a little bit of background and tell you a bit about it in case you don't know what it is. I uh first started to work on software supply chain security back around 2002 or so and in that time like almost no one was paying attention. Um when I first started to release and talk about problems then I actually normally had people at sort of the what would now be kind of the nation state actor hackers reaching out to me to learn more information. conforms to have certain properties and we can add security into the process they're doing then we can actually make security better at the same time while letting them still do compliance. this data how do you make sense of it and how do you collect it right you don't want to just dump it up into like a big um in binary storage you just want to you want to be able to access the things

### Excerpt da transcript

All right, welcome everybody. Uh, I'm Justin Capos. I'm a professor at NYU. I'm also one of the creators of IntoTo. And hi everyone. My name is Alan. I'm a software engineer at a small company and I'm a maintainer of Into. So we're going to be talking to you a bit about Intto and trying to give you a little bit of background and tell you a bit about it in case you don't know what it is. Um, so first of all, uh, we need to talk a little bit about software supply chain and software supply chain attacks. So there's lots of ways to define a software supply chain. I'm not going to read what's on the slide to you, but it's basically um the process by which you make your software, the things that happen, whether these are machines that are going and compiling things, whether they're human developers creating patches and stuff like this, whether it's your lawyer looking over uh a license to decide if they can take open source software. All of these types of things come together to become your software supply chain.

And here's just a really simple example here where um I have a version control system here. Uh there's some testing that's done over it like a llinter is run directly on my source code. And then uh assuming that the llinter is okay with it, then I might proceed to actually go and build the software and then package it and send it out. And real software supply chains will often have many more steps here like I might do fuzzing. I might actually do some unit testing and stuff like this on it. I might be pulling in dependencies from other uh locations and stuff like this. But this is just a really simple example that fits nice on a slide and I hope we can all kind of conceptually understand. Um okay, so we talked about what is a software supply chain. Now let's talk about software supply chain attack. And this is a situation where a a party goes in and uh causes something malicious to happen. Um and in fact in some cases it doesn't even require an external party. In some cases it can be something accidental that occurs but you end up with the process not proceeding and not behaving in the way that you would expect or desire it uh to to happen.

And there's tons and tons of incidents for this. So, for instance, if we just look at version control systems here, there have been a bunch of really um high-profile incidents where in the case of one of them that I'll just happen to bring up where allegedly the NSA broke into Juniper and put a backdoor in a lot of
