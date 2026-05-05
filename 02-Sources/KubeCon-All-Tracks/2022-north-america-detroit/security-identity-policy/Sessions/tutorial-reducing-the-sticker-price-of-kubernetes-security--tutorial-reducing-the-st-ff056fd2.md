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
themes: ["Security", "Kubernetes Core"]
speakers: ["Pushkar Joglekar", "VMware"]
sched_url: https://kccncna2022.sched.com/event/182K6/tutorial-reducing-the-sticker-price-of-kubernetes-security-pushkar-joglekar-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Reducing+the+Sticker+Price+Of+Kubernetes+Security+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Tutorial: Reducing the Sticker Price Of Kubernetes Security - Pushkar Joglekar, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Pushkar Joglekar, VMware
- Schedule: https://kccncna2022.sched.com/event/182K6/tutorial-reducing-the-sticker-price-of-kubernetes-security-pushkar-joglekar-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Reducing+the+Sticker+Price+Of+Kubernetes+Security+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Tutorial: Reducing the Sticker Price Of Kubernetes Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182K6/tutorial-reducing-the-sticker-price-of-kubernetes-security-pushkar-joglekar-vmware
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Reducing+the+Sticker+Price+Of+Kubernetes+Security+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bu93NHRUnhw
- YouTube title: Tutorial: Reducing the Sticker Price Of Kubernetes Security - Pushkar Joglekar, VMware
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tutorial-reducing-the-sticker-price-of-kubernetes-security/bu93NHRUnhw.txt
- Transcript chars: 65261
- Keywords: security, cluster, second, actually, essentially, default, basically, running, profile, container, restricted, standard, change, questions, release, docker, create, images

### Resumo baseado na transcript

my name is pushkar I work as a sub-project maintainer in kubernetes 6 security the sub Project's name is tooling so anything related to security that we do for kubernetes [Music] are we good on audio I hear an echo okay all right so anything that we can do by writing code or helping people write code that is going to improve security for open source kubernetes is what by supposedly lead responsibilities are uh and then the other things are I'll end up helping out other sub projects Etc with kubernetes API it's installing kind so for folks who are not familiar with kind kind stands for kubernetes and Docker and what essentially it's doing is I have a cluster I want to play around with it but creating cluster is hard maintaining it many people from six security and Sig auth which is another Sig as well as many other six in kubernetes have worked for multiple months to make sure this deprecation and eventual removal process is as convenient and simple for anyone who is an end user so hopefully you are aware by now that we have removed it and it's been deprecated for a while anybody using pod security policies there was actually a great talk on how to migrate from an existing set of pod security policies to something like the pawn security admission that we have which happened yesterday I attended it I really loved it they also explained uh something of a policy migrator tool...

### Excerpt da transcript

my name is pushkar I work as a sub-project maintainer in kubernetes 6 security the sub Project's name is tooling so anything related to security that we do for kubernetes [Music] are we good on audio I hear an echo okay all right so anything that we can do by writing code or helping people write code that is going to improve security for open source kubernetes is what by supposedly lead responsibilities are uh and then the other things are I'll end up helping out other sub projects Etc we will have a couple of folks who will help you out if you get stuck especially Tabby who is our chair for sick security who has graciously come out to help out so bit more about me if you saw the photo on the previous slide I'm in the sfb area one of my favorite places to go for a car ride is Mendocino County which is what the sweatshirt is from I really love the coast like I said apart from six security I am also a tech lead for cncf tax security great question to ask what's the difference between tax Securities security during the breaks or after the session I am also recently associate member for kubernetes security response committee so anytime you get a cve uh a notification or we are one of the people who send it out to the haresh of the community I'm formerly a staff security engineer at VMware tanzu like I said I love the Bay Area also I love many things that start with C so cycling chai Indian curries camera and Cricket if anybody follows we have a World Cup going on and you can find more about me on the link on the slide so we will divide it into small blocks uh so that we don't get overwhelmed or get really tired at the end of the session uh this is the intro section we'll have 20 minutes for the first task including the five minute break 25 minutes for the second one with five minute break included and then 30 minutes with five minute break included eventually at the end we will wrap up and I'll share some links for further reading if you want to continue to explore more and more about this so uh just by raising your hand how many of you are on Mac OS right now if you are going to follow okay perfect I have tested this on Mac OS so most of you should hopefully be able to follow along uh how many of you are on M1 Mac OS okay all right and Intel Okay cool so there is in the install prerequisites part there is a small change for people will have to do for once on M1 basically instead of Darwin AMD 64 binaries you will be ensuring Darwin um 64 binaries so we'll tal
