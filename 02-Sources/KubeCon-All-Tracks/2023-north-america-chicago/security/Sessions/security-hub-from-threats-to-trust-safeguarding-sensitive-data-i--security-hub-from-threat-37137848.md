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
themes: ["Security", "Storage Data"]
speakers: ["Moritz Eckert", "Edgeless Systems"]
sched_url: https://kccncna2023.sched.com/event/1SKcd/security-hub-from-threats-to-trust-safeguarding-sensitive-data-in-k8s-moritz-eckert-edgeless-systems
youtube_search_url: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+From+Threats+to+Trust%3A+Safeguarding+Sensitive+Data+in+K8s+CNCF+KubeCon+2023
slides: []
status: parsed
---

# SECURITY HUB: From Threats to Trust: Safeguarding Sensitive Data in K8s - Moritz Eckert, Edgeless Systems

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Storage Data]]
- País/cidade: United States / Chicago
- Speakers: Moritz Eckert, Edgeless Systems
- Schedule: https://kccncna2023.sched.com/event/1SKcd/security-hub-from-threats-to-trust-safeguarding-sensitive-data-in-k8s-moritz-eckert-edgeless-systems
- Busca YouTube: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+From+Threats+to+Trust%3A+Safeguarding+Sensitive+Data+in+K8s+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre SECURITY HUB: From Threats to Trust: Safeguarding Sensitive Data in K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1SKcd/security-hub-from-threats-to-trust-safeguarding-sensitive-data-in-k8s-moritz-eckert-edgeless-systems
- YouTube search: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+From+Threats+to+Trust%3A+Safeguarding+Sensitive+Data+in+K8s+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GCNhtDRGl1I
- YouTube title: SECURITY HUB: From Threats to Trust: Safeguarding Sensitive Data in K8s - Moritz Eckert
- Match score: 0.988
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/security-hub-from-threats-to-trust-safeguarding-sensitive-data-in-k8s/GCNhtDRGl1I.txt
- Transcript chars: 35570
- Keywords: confidential, cluster, course, access, inside, control, concept, provider, information, isolated, context, application, usually, actually, verify, environment, question, security

### Resumo baseado na transcript

yeah thank you pushka um welcome to from threats to trust safeguarding sensitive data in kubernetes hope this is the talk you you all are here for otherwise feel feel free to run um quick introduction about me uh I'm Mor eat I my day job I work at a startup from Germany called ESS systems and there I have the um the pleasure to work with a wonderful team on open source confidential Computing software uh we Al happened to be the organizer of the biggest uh conference in

### Excerpt da transcript

yeah thank you pushka um welcome to from threats to trust safeguarding sensitive data in kubernetes hope this is the talk you you all are here for otherwise feel feel free to run um quick introduction about me uh I'm Mor eat I my day job I work at a startup from Germany called ESS systems and there I have the um the pleasure to work with a wonderful team on open source confidential Computing software uh we Al happened to be the organizer of the biggest uh conference in that space called the open confidential Computing conference um here personally my background is in the software security um vulnerability Discovery um binary exploitation kind of site of things I spent a fair bit of my lifetime in Capture the Flag competitions with team shelish and yeah if I'm not in front of a laptop screen I like to write my my bike a lot um and also enjoy a good cup of of coffee can definitely recommend the uh Intelligencer here in Chicago so if you're into good coffee uh you're welcome definitely check that out but enough about that boring stuff today I want to go on a journey about trust especially trust in our model of cloud computing and as especially on the infrastructure side of things so trust can run very deep if you think about the trust model in our cloud and the infrastructure side think of the the iceberg Meme here right you have your application on top your code your container all the stuff you control that's something you trust uh you hopefully Implement some rigorous testing scanning fuzzing whatever you do to protect your application protect the front door but then of course your application is not Standalone in most cases uh you have some dependencies your code is stored somewhere in a repository some people some U machines have access to that repository and then likely there's some kind of pipeline that takes your code from the repository to a production deployment and all of this of course comes with a certain amount of trust right do you trust the code dependencies usually uh I guess most of you will Implement some form of supply chain security uh you have some access controls you get a repository so you have all of this controls to to reduce the Trust In in these components then we can go one step further uh do you trust the admins the your developers Whoever has access to those dependencies get repository to your code do you actually trust the platform you deploy deploying in do you trust your cloud service provider if your container runs on on on g
