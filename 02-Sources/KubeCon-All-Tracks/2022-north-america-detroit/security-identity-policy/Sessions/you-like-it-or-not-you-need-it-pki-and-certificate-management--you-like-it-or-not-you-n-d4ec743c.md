---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Shweta Vohra", "IBM"]
sched_url: https://kccncna2022.sched.com/event/182KC/you-like-it-or-not-you-need-it-pki-and-certificate-management-shweta-vohra-ibm
youtube_search_url: https://www.youtube.com/results?search_query=You+Like+It+Or+Not%3B+You+Need+It%21+-+PKI+And+Certificate+Management+CNCF+KubeCon+2022
slides: []
status: parsed
---

# You Like It Or Not; You Need It! - PKI And Certificate Management - Shweta Vohra, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: United States / Detroit
- Speakers: Shweta Vohra, IBM
- Schedule: https://kccncna2022.sched.com/event/182KC/you-like-it-or-not-you-need-it-pki-and-certificate-management-shweta-vohra-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=You+Like+It+Or+Not%3B+You+Need+It%21+-+PKI+And+Certificate+Management+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre You Like It Or Not; You Need It! - PKI And Certificate Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182KC/you-like-it-or-not-you-need-it-pki-and-certificate-management-shweta-vohra-ibm
- YouTube search: https://www.youtube.com/results?search_query=You+Like+It+Or+Not%3B+You+Need+It%21+-+PKI+And+Certificate+Management+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SJ0d3GIfSZo
- YouTube title: You Like It Or Not; You Need It! - PKI And Certificate Management - Shweta Vohra, IBM
- Match score: 0.958
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/you-like-it-or-not-you-need-it-pki-and-certificate-management/SJ0d3GIfSZo.txt
- Transcript chars: 28264
- Keywords: certificate, certificates, authority, public, private, network, digital, provides, server, spiffy, secure, intermediate, request, secured, workloads, design, identity, communication

### Resumo baseado na transcript

hello cubecon and Cloud nativecon hi to everyone I'm shweta bhora I am an architect in Winter blogger AWS Community Builder open source Enthusiast and contributor at times before I start with this session I must say what a phenomenal week this has been we all have gained observed and interacted so much it's time after today to go back and see who and reflect back what we have gained in this amazing cubecon and Cloud nativecon before we go back today it's time for this session and it's about

### Excerpt da transcript

hello cubecon and Cloud nativecon hi to everyone I'm shweta bhora I am an architect in Winter blogger AWS Community Builder open source Enthusiast and contributor at times before I start with this session I must say what a phenomenal week this has been we all have gained observed and interacted so much it's time after today to go back and see who and reflect back what we have gained in this amazing cubecon and Cloud nativecon before we go back today it's time for this session and it's about you like it a lot you need it pki and certificate management let's get started the contents which I'm planning to cover in this session are vocabulary and repressure about pki and certificate management vocabulary for those who are new to this topic and refresher for those who are might be aware of but they might learn a few things new from this we are also going to talk about a case study which is common yet complex production case study and a demonstration and we will be ending with the five pki design decisions that you must know okay so here we are with the vocabulary and repression pki public key infrastructure what is pki let's understand that always when you communicate over Network you have two endpoints this could be client and server now these endpoints talk to each other let's say you are talk you are using a internet banking or a bank site where you are doing internet banking and this happens over secure socket layer or transport layer security is required and that protocol is used what this client and server how they trust each other and to do what do they need there are two things primarily any end point or two endpoints need from each other so that they can smoothly talk to each other the first one is the trust establishment client needs to know that the server I'm talking to or let's say the bank site I'm talking to is secured enough that I can share my data as information and once that trust is established you need to exchange the encrypted data over Network now this happens day in and out when they indirect over that work but what happens behind the scene how does pki come in picture let's look at that to have that trust established your server needs some authorities the first and foremost the certificate Authority registration Authority and the verification Authority what the server does is that it requests the registration authority to issue and assign certificate to the server using which it can give trust to the client that yes it has a digital cer
