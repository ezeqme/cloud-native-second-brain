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
themes: ["Security", "Storage Data", "Kubernetes Core"]
speakers: ["Christophe Tafani-Dereeper", "Frederic Baguelin", "Datadog"]
sched_url: https://kccnceu2024.sched.com/event/1YeRs/keep-hackers-out-of-your-cluster-with-these-5-simple-tricks-christophe-tafani-dereeper-frederic-baguelin-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Keep+Hackers+Out+of+Your+Cluster+with+These+5+Simple+Tricks+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keep Hackers Out of Your Cluster with These 5 Simple Tricks - Christophe Tafani-Dereeper & Frederic Baguelin, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Christophe Tafani-Dereeper, Frederic Baguelin, Datadog
- Schedule: https://kccnceu2024.sched.com/event/1YeRs/keep-hackers-out-of-your-cluster-with-these-5-simple-tricks-christophe-tafani-dereeper-frederic-baguelin-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Keep+Hackers+Out+of+Your+Cluster+with+These+5+Simple+Tricks+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keep Hackers Out of Your Cluster with These 5 Simple Tricks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRs/keep-hackers-out-of-your-cluster-with-these-5-simple-tricks-christophe-tafani-dereeper-frederic-baguelin-datadog
- YouTube search: https://www.youtube.com/results?search_query=Keep+Hackers+Out+of+Your+Cluster+with+These+5+Simple+Tricks+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UZz44j8bszU
- YouTube title: Keep Hackers Out of Your Cluster with These 5 Simp... Christophe Tafani-Dereeper & Frederic Baguelin
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keep-hackers-out-of-your-cluster-with-these-5-simple-tricks/UZz44j8bszU.txt
- Transcript chars: 30934
- Keywords: directly, threat, cluster, security, attacker, manage, actually, container, credentials, internet, workload, basically, secure, access, attack, create, vulnerabilities, thanks

### Resumo baseado na transcript

thanks everyone from uh for coming here um so today we're going to be talking about uh how to keep hackers out of your clusters with five simple tricks and obviously it's not going to be five simple tricks um so before we start I want to pull the room a little bit who would identify as someone who's doing mostly security security engineering pester right um more on the S devop devops engineer side system engineer and more on the application development side software engineer okay great quite diverse

### Excerpt da transcript

thanks everyone from uh for coming here um so today we're going to be talking about uh how to keep hackers out of your clusters with five simple tricks and obviously it's not going to be five simple tricks um so before we start I want to pull the room a little bit who would identify as someone who's doing mostly security security engineering pester right um more on the S devop devops engineer side system engineer and more on the application development side software engineer okay great quite diverse audence cool so thanks for being here today um so the goal and what we try to do today is to start from this state so you are someone who has to run applications in cuties and you want to make sure that whenever someone asks you to secure it uh you don't feel like this but you have instead uh you know that you can feel confident and you know how to prioritize thing and that instead you can feel like that my name is Kristoff I'm French as you can hear I live in Switzerland and I work at data dog focusing on cloud security and open source I'm the maintainer of a few open source projects one is called the stratus Rim another one is called the manage kubernetes auditing toolkit and this is Fred hi I'm Fred uh I'm senior security researcher at datadog mainly focusing on threat intelligence manare analysis and yeah threat activities great so on the agenda we have mostly three things the first one is we're going to do a bit of fret modeling of kubernetes it sounds like a swear world but it's going to be fine don't worry and then we're going to look at uh Fred is going to tell us a bit at okay the first one is the theoretical side but then what do we see in the wild what do we see in the real world how are attackers actually doing things and finally based on that we're going to say well these are the things that make sense to implement because uh they are actually valuable we are making two assumptions the first one is that we are using managed kubernetes running in the cloud so eks AKs or GK uh just because you know it's a different level of abstraction and it allows us to say for instance that itcd is going to be secure and we don't need to care about that who's using manage kubernetes in one of the maor clouds okay many people not everyone but it will still be relevant uh if you are using your own on your Raspberry p so FR modeling um again if we want a bad user story to start with it's just that someone who defends something I need to be able to understand what are
