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
themes: ["AI ML", "Security"]
speakers: ["Francesco Minna", "Vrije Universiteit Amsterdam", "Agathe Blaise", "Thales SIX"]
sched_url: https://kccnceu2024.sched.com/event/1YeOu/misconfigurations-in-helm-charts-how-far-are-we-from-automated-detection-and-mitigation-francesco-minna-vrije-universiteit-amsterdam-agathe-blaise-thales-six
youtube_search_url: https://www.youtube.com/results?search_query=Misconfigurations+in+Helm+Charts%3A+How+Far+Are+We+from+Automated+Detection+and+Mitigation%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Misconfigurations in Helm Charts: How Far Are We from Automated Detection and Mitigation? - Francesco Minna, Vrije Universiteit Amsterdam & Agathe Blaise, Thales SIX

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: France / Paris
- Speakers: Francesco Minna, Vrije Universiteit Amsterdam, Agathe Blaise, Thales SIX
- Schedule: https://kccnceu2024.sched.com/event/1YeOu/misconfigurations-in-helm-charts-how-far-are-we-from-automated-detection-and-mitigation-francesco-minna-vrije-universiteit-amsterdam-agathe-blaise-thales-six
- Busca YouTube: https://www.youtube.com/results?search_query=Misconfigurations+in+Helm+Charts%3A+How+Far+Are+We+from+Automated+Detection+and+Mitigation%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Misconfigurations in Helm Charts: How Far Are We from Automated Detection and Mitigation?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOu/misconfigurations-in-helm-charts-how-far-are-we-from-automated-detection-and-mitigation-francesco-minna-vrije-universiteit-amsterdam-agathe-blaise-thales-six
- YouTube search: https://www.youtube.com/results?search_query=Misconfigurations+in+Helm+Charts%3A+How+Far+Are+We+from+Automated+Detection+and+Mitigation%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ec4koZDe1b4
- YouTube title: Misconfigurations in Helm Charts: How Far Are We from Automated Detection and Mitigation?
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/misconfigurations-in-helm-charts-how-far-are-we-from-automated-detecti/ec4koZDe1b4.txt
- Transcript chars: 21038
- Keywords: actually, permission, misconfigurations, configuration, container, needed, functionality, output, charts, application, policies, containers, default, finally, running, functionalities, remove, capabilities

### Resumo baseado na transcript

good afternoon everyone welcome back from the lunch break and welcome to this uh talk okay welcome to this talk which is about misconfigurations in hand charts and how far are we from automated detection and mitigation and uh today with me there is a gut so hello everyone so my name is agat blaz I'm a research engineer working at Tes and I mostly work working on the virtualization of network system and the security of such systems and I'm Franchesco and I'm doing a PhD at the Free

### Excerpt da transcript

good afternoon everyone welcome back from the lunch break and welcome to this uh talk okay welcome to this talk which is about misconfigurations in hand charts and how far are we from automated detection and mitigation and uh today with me there is a gut so hello everyone so my name is agat blaz I'm a research engineer working at Tes and I mostly work working on the virtualization of network system and the security of such systems and I'm Franchesco and I'm doing a PhD at the Free University of Amsterdam and very brief advertise advertisements before we dive into the technical content this work was actually part of a collaboration in a European project I sure most just finished and the new project SEC for I for sec I put the link there so we're always looking for a collabor operations especially with companies if you're interested in the what we're doing please check it out um so now diving into the content of this talk uh which is misconfigurations in uh the cloud why should we care in the first place well because from recent reports um they found that uh such misconfigurations can be the reason for several incidents security incidents and um because they uh they containers that actually run your applications they also usually run for a very limited time so the the runtime window for detection and the mitigation is short and so at the beginning we we started this work saying okay because we have this very limited time window at runtime let's see how much we can improve uh before uh reaching runtime so at static time uh and also the other reasons where uh because there are a lot of uh tools that can analyze configuration files hand charts as well uh however there are some inconsistencies between the output of such tools and also there is no indication about whether a configuration might break the functionality of your application or not um and because misconfigurations can uh cause bad things so to say uh there are some Frameworks available that uh give a list of best practices and security recommendations that you should follow with your configurations for example the CIS Benchmark or the NSA and cisa hardening guides and they for example suggest that you should not run your container uh as root minimize the capabilities the Linux capability you assigned and so on and uh looking at an example uh on on the left of the slide you can see a a snippet of a yaml file that can be used used to deploy a deployment resource uh on a cluster and as you can see there
