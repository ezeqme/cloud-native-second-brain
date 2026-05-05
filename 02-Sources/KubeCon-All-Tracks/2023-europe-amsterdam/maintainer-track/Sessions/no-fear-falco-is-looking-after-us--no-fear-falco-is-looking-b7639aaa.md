---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Jason Dellaluce", "Luca Guerra", "Sysdig", "Melissa Kilby", "Apple", "Carlos Panato", "Chainguard", "Hendrik Brueckner", "IBM"]
sched_url: https://kccnceu2023.sched.com/event/1HyTj/no-fear-falco-is-looking-after-us-jason-dellaluce-luca-guerra-sysdig-melissa-kilby-apple-carlos-panato-chainguard-hendrik-brueckner-ibm
youtube_search_url: https://www.youtube.com/results?search_query=No+Fear%2C+Falco+Is+Looking+After+Us%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# No Fear, Falco Is Looking After Us! - Jason Dellaluce & Luca Guerra, Sysdig; Melissa Kilby, Apple; Carlos Panato, Chainguard; Hendrik Brueckner, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jason Dellaluce, Luca Guerra, Sysdig, Melissa Kilby, Apple, Carlos Panato, Chainguard, Hendrik Brueckner, IBM
- Schedule: https://kccnceu2023.sched.com/event/1HyTj/no-fear-falco-is-looking-after-us-jason-dellaluce-luca-guerra-sysdig-melissa-kilby-apple-carlos-panato-chainguard-hendrik-brueckner-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=No+Fear%2C+Falco+Is+Looking+After+Us%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre No Fear, Falco Is Looking After Us!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyTj/no-fear-falco-is-looking-after-us-jason-dellaluce-luca-guerra-sysdig-melissa-kilby-apple-carlos-panato-chainguard-hendrik-brueckner-ibm
- YouTube search: https://www.youtube.com/results?search_query=No+Fear%2C+Falco+Is+Looking+After+Us%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=z_iRCkp4Cp0
- YouTube title: No Fear, Falco Is Looking After Us! - Jason & Luca, Melissa, Carlos, Hendrik
- Match score: 0.74
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/no-fear-falco-is-looking-after-us/z_iRCkp4Cp0.txt
- Transcript chars: 31044
- Keywords: security, kernel, course, maintainers, basically, mentioned, github, support, release, modern, pretty, melissa, question, maintainer, testing, container, thanks, working

### Resumo baseado na transcript

good afternoon everyone and welcome to the Falco maintenance track we have a full house here and five maintainers myself I'm Melissa Luca Jason Carlos and Hendrick we have a lot of content to cover let's get started if you have never heard of hanco think of it as security cameras for your operating system to detect harmful Behavior Falco uses rules to Define behavior allowing you to customize them for your needs from a technical perspective Falco resides low on the stack at the Linux kernel layer using modern

### Excerpt da transcript

good afternoon everyone and welcome to the Falco maintenance track we have a full house here and five maintainers myself I'm Melissa Luca Jason Carlos and Hendrick we have a lot of content to cover let's get started if you have never heard of hanco think of it as security cameras for your operating system to detect harmful Behavior Falco uses rules to Define behavior allowing you to customize them for your needs from a technical perspective Falco resides low on the stack at the Linux kernel layer using modern Technologies like extended Berkeley packet filter ebpf it's a pretty cool way of doing kernel programming which raises the question why do we need kernel programming in the first place looking back to what evpf does it can attach to Linux kernel Trace points to monitor system calls and more you may ask yourself what our system calls and why do we need them to detect cyber intrusions so if you really think about cyber security if you attack the system like the way think of an operating system at the lower kernel level with all the applications running on top and there is an analogy you can think about it if you've watched stranger things on Netflix imagine it like being in Underworld in an upper world with a Gateway in between so system calls are the API or largest Gateway to ask the parental for permission to interact with Hardware such as accessing memory or opening a file from disk Falco hooks into system calls to detect malicious behavior and send an alert from the precise location on the stack where it's the most beneficial to send an alert from and furthermore Falco lets you customize your deployments with your custom rules and that way you can determine what is happening in your environments and to we as maintainers we benefit from Falco to make our deployments more stable and scale it out more and um there's also another aspect to it if you um want to um so besides system calls there is a lot more to Falco starting from the past year Falco introduced a new plugin system that basically allows everyone to develop extension for Falco and basically adapt the tool to many more use cases this mainly gives us the opportunity to pipe new data sources into Falco and write security rules on top of those one specifically important new data source type is for example Cloud logging so that you potentially can use that to execute the rules in any services like Amazon cloudtrail or kubernetes audioblocks starting about examples of those Integrations those two
