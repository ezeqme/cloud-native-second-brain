---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security"]
speakers: ["Rafik Harabi", "Sysdig"]
sched_url: https://kccncna2023.sched.com/event/1R2nA/cloud-native-application-threat-modeling-and-adversary-emulation-techniques-and-tools-rafik-harabi-sysdig
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Application+Threat+Modeling+and+Adversary+Emulation+%3A+Techniques+and+Tools+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cloud Native Application Threat Modeling and Adversary Emulation : Techniques and Tools - Rafik Harabi, Sysdig

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Rafik Harabi, Sysdig
- Schedule: https://kccncna2023.sched.com/event/1R2nA/cloud-native-application-threat-modeling-and-adversary-emulation-techniques-and-tools-rafik-harabi-sysdig
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Application+Threat+Modeling+and+Adversary+Emulation+%3A+Techniques+and+Tools+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cloud Native Application Threat Modeling and Adversary Emulation : Techniques and Tools.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nA/cloud-native-application-threat-modeling-and-adversary-emulation-techniques-and-tools-rafik-harabi-sysdig
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Application+Threat+Modeling+and+Adversary+Emulation+%3A+Techniques+and+Tools+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=artdWYR4jkU
- YouTube title: Cloud Native Application Threat Modeling and Adversary Emulation : Techniques and... - Rafik Harabi
- Match score: 0.984
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cloud-native-application-threat-modeling-and-adversary-emulation-techn/artdWYR4jkU.txt
- Transcript chars: 32798
- Keywords: container, thread, access, application, kubernets, define, defining, techniques, attack, finally, coming, someone, modeling, adversary, security, trying, another, everything

### Resumo baseado na transcript

hello I all um thank you for joining me um this afternoon for this talk entitled Cloud native thread modeling and adversary imulation um technique Cals my name is Rafi kabi I've been the it w for almost 15 years and I've been with s for um three year and a half right now uh working mainly with a customer in Europe and Middle East on cloud native security advocacy and moving them security to the cloud um before that I've been working on Consulting go through Cloud programs mainly starting uh learning adversary imidation for for kubernets um Caldera Caldera is a complementary Tool uh for atom great team so they they offering this kind of automation around um adversary um imulation so um they have a building Behavior M to ATT track so you can choose one of the scenario or multiple scenario and you can run this scenario in an automated way Gathering the logs and spot what what is missing for your system so this is really interesting when you want to to start automating the

### Excerpt da transcript

hello I all um thank you for joining me um this afternoon for this talk entitled Cloud native thread modeling and adversary imulation um technique Cals my name is Rafi kabi I've been the it w for almost 15 years and I've been with s for um three year and a half right now uh working mainly with a customer in Europe and Middle East on cloud native security advocacy and moving them security to the cloud um before that I've been working on Consulting go through Cloud programs mainly with cons companies like de and entity data so there is my LinkedIn profile uh my future please feel free to uh to to reach me so uh what we'll be talking about today we start by talking about the cloud native application building blocks how it's different from the Legacy uh world uh then we Del into the multitude of a cloud attack surface and the different challenges that it come with um then we uh deep into the thread modeling uh the different techniques that we use for the thread modeling following by the adversary emulation for cloud native application and finally you finish by listing the tool that will help you uh to do this stuff plus um takeaways so let's start um on open time um it was like quite simple uh to protect montic application they are deployed in kind of VM or physical services and what you need to do just putting a kind of firewall or EDM in front of it to detect any inion but this is a little bit different or totally different when it come uh to the cloud first because the cloud services are public they are exposed to the outside board you have different Services they are leing together um in your Cloud account or your Cloud project organization and you need to define the right control access for each team or each service um also um this this complexity of mple services talking together uh generate a lot uh flogs and it will be really hard to detect an unusual activity um let's see how Cloud native application is B so we have the cloud infrastructure then we have the workload can be containers serverless maybe some work CLS coming from on Prem just shift and lift and all this stuff is working on top of kubernets um whatever is is managed by your teams or you're taking one manager service from the cloud provider or container as a service and we have a bch of um let's say um satell services that you need for um your application mainly everything around identity and access Network like load balancing and so on Management Services like logging and monitoring and fi
