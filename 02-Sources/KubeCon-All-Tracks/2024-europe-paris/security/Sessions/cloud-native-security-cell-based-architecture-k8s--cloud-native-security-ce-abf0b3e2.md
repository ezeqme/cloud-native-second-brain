---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security"]
speakers: ["Rostyslav Myronenko", "Shweta Vohra", "Booking.com"]
sched_url: https://kccnceu2024.sched.com/event/1YePJ/cloud-native-security-cell-based-architecture-k8s-rostyslav-myronenko-shweta-vohra-bookingcom
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Security%3A+Cell-Based+Architecture+%26+K8s+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cloud Native Security: Cell-Based Architecture & K8s - Rostyslav Myronenko & Shweta Vohra, Booking.com

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: Rostyslav Myronenko, Shweta Vohra, Booking.com
- Schedule: https://kccnceu2024.sched.com/event/1YePJ/cloud-native-security-cell-based-architecture-k8s-rostyslav-myronenko-shweta-vohra-bookingcom
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Security%3A+Cell-Based+Architecture+%26+K8s+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cloud Native Security: Cell-Based Architecture & K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePJ/cloud-native-security-cell-based-architecture-k8s-rostyslav-myronenko-shweta-vohra-bookingcom
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Security%3A+Cell-Based+Architecture+%26+K8s+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=z8KLVZBHK-E
- YouTube title: Cloud Native Security: Cell-Based Architecture & K8s - Rostyslav Myronenko & Shweta Vohra
- Match score: 0.828
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cloud-native-security-cell-based-architecture-k8s/z8KLVZBHK-E.txt
- Transcript chars: 25526
- Keywords: architecture, security, another, outside, cell-based, multiple, domain, design, inside, particular, instance, payment, driven, internal, challenges, requirements, address, native

### Resumo baseado na transcript

hello everyone thank you for joining our session we are so excited to be in Paris to be at cucon and uh to be speakers today uh personally me it's my first time to be a speaker in such a big conference like cucon that's why I'm slightly nervous but still excited and today thank you thank you and today we will contact a talk about the cellb architecture or the CBA and we will uh first talk about what it what is the CBA then uh we will share

### Excerpt da transcript

hello everyone thank you for joining our session we are so excited to be in Paris to be at cucon and uh to be speakers today uh personally me it's my first time to be a speaker in such a big conference like cucon that's why I'm slightly nervous but still excited and today thank you thank you and today we will contact a talk about the cellb architecture or the CBA and we will uh first talk about what it what is the CBA then uh we will share with you what were our business drivers uh for using the svest architecture then we will move forward with the case study where we will present our solution architecture there and in the end we will share with you uh learning which we uh got by uh working with the CBA before we proceed let us introduce ourselves my name is Rosy and I'm A Cloud Solutions architect from uh booking.com mostly uh working with AWS and kubernetes the thing is uh I think in the speaker agenda I mentioned as nine ad certified but I become the full El certified recently so I just like cloud and Cloud native and now uh sh can us introduce yourself thank you rosty good afternoon everyone how are you all doing great so as rosty said we both are solution architect from booking.com so first question I would like to ask how many of you love love to travel a raise of hand almost any of us that's great uh because booking.com if you know uh we have a mission to make it easier for everyone to experience the world and with that mission in mind uh we are very selective about our Technologies and um working towards it and of course open source technologies have a bigger role to play in that uh apart from that I'm um more interested in security talks so that's why this talk as well around security um but we can catch up later on that if anything you want to introduce to us with that said let's dive into our topic for today this is about cell-based architecture cell-based architecture um is essentially a decentralized architecture reference which was first introduced by wso2 open-source group and since then it uh really picked up well and adopted by us as well before we see the details of cell-based architecture I would like to uh delve on the point that why cell-based architecture we at some point between 2014 to 2020 we said that monoliths are not good they are centralized though they are good in some sense but um we want to move away from monoliths and that's where we came more towards microservices and containers and container orchestration world but when w
