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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Adolfo García Veytia", "Stacklok", "Kat Cosgrove", "Dell Technologies", "Carlos Panato", "Chainguard", "Joseph Sandoval", "Adobe"]
sched_url: https://kccnceu2024.sched.com/event/1YhfZ/planning-for-maturity-sig-releases-revamp-for-a-more-stable-kubernetes-adolfo-garcia-veytia-stacklok-kat-cosgrove-dell-technologies-carlos-panato-chainguard-joseph-sandoval-adobe
youtube_search_url: https://www.youtube.com/results?search_query=Planning+for+Maturity%3A+SIG+Release%27s+Revamp+for+a+More+Stable+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Planning for Maturity: SIG Release's Revamp for a More Stable Kubernetes - Adolfo García Veytia, Stacklok; Kat Cosgrove, Dell Technologies; Carlos Panato, Chainguard; Joseph Sandoval, Adobe

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Adolfo García Veytia, Stacklok, Kat Cosgrove, Dell Technologies, Carlos Panato, Chainguard, Joseph Sandoval, Adobe
- Schedule: https://kccnceu2024.sched.com/event/1YhfZ/planning-for-maturity-sig-releases-revamp-for-a-more-stable-kubernetes-adolfo-garcia-veytia-stacklok-kat-cosgrove-dell-technologies-carlos-panato-chainguard-joseph-sandoval-adobe
- Busca YouTube: https://www.youtube.com/results?search_query=Planning+for+Maturity%3A+SIG+Release%27s+Revamp+for+a+More+Stable+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Planning for Maturity: SIG Release's Revamp for a More Stable Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhfZ/planning-for-maturity-sig-releases-revamp-for-a-more-stable-kubernetes-adolfo-garcia-veytia-stacklok-kat-cosgrove-dell-technologies-carlos-panato-chainguard-joseph-sandoval-adobe
- YouTube search: https://www.youtube.com/results?search_query=Planning+for+Maturity%3A+SIG+Release%27s+Revamp+for+a+More+Stable+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UhIXUarNPKc
- YouTube title: Planning for Maturity: SIG Release's Revamp for a More Stable Kubernetes
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/planning-for-maturity-sig-releases-revamp-for-a-more-stable-kubernetes/UhIXUarNPKc.txt
- Transcript chars: 19801
- Keywords: release, projects, information, security, little, better, github, deadline, working, vulnerability, releases, currently, everything, fantastic, together, planning, engineer, changes

### Resumo baseado na transcript

welcome everyone uh this uh is the Sig release kubernets Sig release uh maintainance track talk uh my name is Carlos panato in my right side here is we have cat and Joseph and in my left side if I'm can do the the hands correctly is a F1 and F12 yeah uh we're going to introduce the Sig release uh itself the team uh it's composed by two teams like two sub teams one is the first the release team it's self that's are fancy and everybody lovees and kubernetes itself like it's easy to use is I think is well documented but we can talk this later and uh I want to call Action here is like most of the people doesn't know like uh what the release engineer like take care those

### Excerpt da transcript

welcome everyone uh this uh is the Sig release kubernets Sig release uh maintainance track talk uh my name is Carlos panato in my right side here is we have cat and Joseph and in my left side if I'm can do the the hands correctly is a F1 and F12 yeah uh we're going to introduce the Sig release uh itself the team uh it's composed by two teams like two sub teams one is the first the release team it's self that's are fancy and everybody lovees and nice and the other one is the release engineer that is like we under under the ground like no one wants to work with us but I think you should join us I'm going to pass the the next slides to Cat hello I like this mic better so uh the release team changes a lot over time and we're getting better at it every cycle every cycle something goes wrong and uh we fix it in the next one so previously until this current release version 130 the release team was made up of six sub teams but when we moved all of our like internal planning and project management to GitHub project boards it uh reduced the workload for the bug triage team so severely that they had almost nothing to do so we decided to merge them with the CI signal team into the new release signal team um which is going going pretty well it's uh a little bit stressful because that is a team that is busy like the entire cycle um they always have something to do but it is better than having uh one team doing nothing uh for the whole release so we consider ourselves to be doing a good job when we manag to like automate A team out of existence this is the second time we've done it I think so we're pretty pretty proud of that one this team is also changing the way we handle documentation so uh documentation is not optional if your kep has user-facing changes those changes have to be documented it is it is a hard requirement um and we're we're going to be pretty inflexible on that one to make this more clear uh we have introduced a docs freeze previously the last deadline for documentation in a release cycle was called the PR's ready to merge deadline and people treated this deadline as though it was very soft um it's always kind of a struggle to get to document in and reviewed on time which is real stressful for both the release docs team and Sig docs who have to review that documentation so to make it clear that this is a requirement we've moved the docs deadline more in line with our enhancements deadlines so like enhancements freeze and code freeze this is a real hard
