---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Novice"
themes: ["AI ML", "Security"]
speakers: ["Joshua Lock", "Verizon"]
sched_url: https://kccnceu2024.sched.com/event/1YeMA/an-acronym-free-introduction-to-software-supply-chain-security-joshua-lock-verizon
youtube_search_url: https://www.youtube.com/results?search_query=An+Acronym+Free+Introduction+to+Software+Supply+Chain+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# An Acronym Free Introduction to Software Supply Chain Security - Joshua Lock, Verizon

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: France / Paris
- Speakers: Joshua Lock, Verizon
- Schedule: https://kccnceu2024.sched.com/event/1YeMA/an-acronym-free-introduction-to-software-supply-chain-security-joshua-lock-verizon
- Busca YouTube: https://www.youtube.com/results?search_query=An+Acronym+Free+Introduction+to+Software+Supply+Chain+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre An Acronym Free Introduction to Software Supply Chain Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMA/an-acronym-free-introduction-to-software-supply-chain-security-joshua-lock-verizon
- YouTube search: https://www.youtube.com/results?search_query=An+Acronym+Free+Introduction+to+Software+Supply+Chain+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1PKZGn0eoZE
- YouTube title: An Acronym Free Introduction to Software Supply Chain Security - Joshua Lock, Verizon
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/an-acronym-free-introduction-to-software-supply-chain-security/1PKZGn0eoZE.txt
- Transcript chars: 33125
- Keywords: software, security, supply, source, dependencies, package, secure, provide, dependency, process, production, someone, whether, images, infrastructure, content, projects, release

### Resumo baseado na transcript

good afternoon everybody um there are an awful lot of talks here so thank you for taking the time to attend mine my name is Joshua Lo I'm going to try and provide an acronym free introduction to software supply chain security which is a lot of words to say and um that's why pretty much why I wanted to give this talk is there's there's a lot of interest in sofware supply chain security um governments and organizations around the world are increasingly focused on it and I wanted

### Excerpt da transcript

good afternoon everybody um there are an awful lot of talks here so thank you for taking the time to attend mine my name is Joshua Lo I'm going to try and provide an acronym free introduction to software supply chain security which is a lot of words to say and um that's why pretty much why I wanted to give this talk is there's there's a lot of interest in sofware supply chain security um governments and organizations around the world are increasingly focused on it and I wanted to try and kind of provide a um a cloud native novice introduction to the problems and the ways we can go about solving them um while avoiding any of the acronym soup that any technical domain tends to inherit so my name is Joshua Lo I'm an a software engineer in Verizon's open source program office and I'm going to start with an introduction to um software Supply chains and uh the security of them so soft supply chain what what is a software supply chain it's effectively all of the steps that go into producing uh a piece of software so you will have someone writing some code they'll push the code somewhere hopefully a revision control system uh the code will get picked up and built by uh hopefully some kind of automation um it will pull in a bunch of dependencies uh increasingly many dependencies in this day and age and it will produce some kind of artifact packaged up that it then sends somewhere to be run and this is a nice simple model for what a software supply chain is but of course in reality they are much more complex they um each dependency we pull into our package has its own set of dependencies typically um and there of course additional complexities in that there are boundaries of where our common tools uh can observe so the language package managers we typically interact with when we're building software um don't uh connects into the operating system package managers that Pro Prov provide the base images that we're running our um software on and of course the infrastructure that sits underneath that so this even this diagram uh is a relatively simple view of software supply chain security or a software supply chain sorry and if we want to think about securing uh software supply chain it's it's useful to have a shared understanding of what that means um most people when they talk about software supply chain security they're really thinking about how can they protect against unintended modifications of some software and I really like this diagram uh this is tamper resistan
