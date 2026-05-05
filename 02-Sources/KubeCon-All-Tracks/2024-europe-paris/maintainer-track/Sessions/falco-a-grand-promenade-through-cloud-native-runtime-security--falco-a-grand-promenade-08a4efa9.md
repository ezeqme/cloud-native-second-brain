---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Runtime Containers", "Community Governance"]
speakers: ["Luca Guerra", "Leonardo Grasso", "Jason Dellaluce", "Sysdig", "Carlos Tadeu Panato Junior", "Chainguard", "Melissa Kilby", "Apple"]
sched_url: https://kccnceu2024.sched.com/event/1YhfE/falco-a-grand-promenade-through-cloud-native-runtime-security-luca-guerra-leonardo-grasso-jason-dellaluce-sysdig-carlos-tadeu-panato-junior-chainguard-melissa-kilby-apple
youtube_search_url: https://www.youtube.com/results?search_query=Falco%3A+A+Grand+Promenade+Through+Cloud+Native+Runtime+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Falco: A Grand Promenade Through Cloud Native Runtime Security - Luca Guerra, Leonardo Grasso & Jason Dellaluce, Sysdig; Carlos Tadeu Panato Junior, Chainguard; Melissa Kilby, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Luca Guerra, Leonardo Grasso, Jason Dellaluce, Sysdig, Carlos Tadeu Panato Junior, Chainguard, Melissa Kilby, Apple
- Schedule: https://kccnceu2024.sched.com/event/1YhfE/falco-a-grand-promenade-through-cloud-native-runtime-security-luca-guerra-leonardo-grasso-jason-dellaluce-sysdig-carlos-tadeu-panato-junior-chainguard-melissa-kilby-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Falco%3A+A+Grand+Promenade+Through+Cloud+Native+Runtime+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Falco: A Grand Promenade Through Cloud Native Runtime Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhfE/falco-a-grand-promenade-through-cloud-native-runtime-security-luca-guerra-leonardo-grasso-jason-dellaluce-sysdig-carlos-tadeu-panato-junior-chainguard-melissa-kilby-apple
- YouTube search: https://www.youtube.com/results?search_query=Falco%3A+A+Grand+Promenade+Through+Cloud+Native+Runtime+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iLCBrJgPxJM
- YouTube title: Falco: A Grand Promenade Through Cloud Native Runtime Security - Panel
- Match score: 1.033
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/falco-a-grand-promenade-through-cloud-native-runtime-security/iLCBrJgPxJM.txt
- Transcript chars: 22651
- Keywords: kernel, security, basically, plug-in, plugins, driver, events, performance, making, fields, working, native, detection, server, information, ecosystem, features, ebpf

### Resumo baseado na transcript

welcome everyone to the Falcon man track if you are joining us today you likely want to explore FAL evolution in Cloud native rtime security our journey started in 2016 when Falco created bistic set a new standard in Linux Security in 2018 Falco became the first ever and time security project incubated by the cncf and thanks to Strong adoption contribution 2 years later it was elevated to the incubation level but there is more in 2021 the plug-in system was introduced expanding the Falco domains allowing monitoring Cloud

### Excerpt da transcript

welcome everyone to the Falcon man track if you are joining us today you likely want to explore FAL evolution in Cloud native rtime security our journey started in 2016 when Falco created bistic set a new standard in Linux Security in 2018 Falco became the first ever and time security project incubated by the cncf and thanks to Strong adoption contribution 2 years later it was elevated to the incubation level but there is more in 2021 the plug-in system was introduced expanding the Falco domains allowing monitoring Cloud logs and enabling threat detection in Cloud platform shortly after that Falco cattle our ecosystem tool made it easy to deploy and manage rules and plugins in 2013 and the modern BPF driver based on the compile ones run everywhere technology was introduced making a liap forward in our K instrumentation the last year we also introduced the rules maturity framework to provide standardization and guidance to our adopter and the driver kernal testing framework to ensure broadest Falco compatibility these are just some initiatives that underscore Falco roles and Falco Innovation contribution in the cloud native landscape but Falco is not just about technology it is also about people to make this explicit two years ago we enhanced our governance and formalized the value that have shaped Falon into an open respectful diverse transparent and Vibrant Community our commitment to openness has always been the Project's power and a call for everyone to join our journey by the way our journey holds a moment a milestone that underscore the fal essential roles in Cloud native thanks to our cncf sponsor Emily Fox and Justin cormack thanks to anyone has ever raised an issue opened up request or just participated in our communities thank to you all we have reached the highest the highest level in within the cncf Falon FAL is now a graduated project thank you all thank you thanks a lot uh thank you Leo so uh we know that uh the work that we did with the community with the cncf and with everyone pretty much to get Falco to the point of graduation was something that we all maintainers were involved in but that didn't really stop the usual Falco programming which means uh delivering new features delivering improvements to all pretty much every ECT of our project so in the next few minutes myself and Jason Carlos and Melissa will tell you a bit more about that a bit more about what we did lately apart from making Falco graduate so uh where where are which are the
