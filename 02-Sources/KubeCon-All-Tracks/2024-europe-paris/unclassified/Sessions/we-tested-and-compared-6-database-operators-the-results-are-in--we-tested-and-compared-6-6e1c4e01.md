---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Jérôme Petazzoni", "Tiny Shell Script LLC", "Alexandre Buisine", "Enix"]
sched_url: https://kccnceu2024.sched.com/event/1YeO5/we-tested-and-compared-6-database-operators-the-results-are-in-jerome-petazzoni-tiny-shell-script-llc-alexandre-buisine-enix
youtube_search_url: https://www.youtube.com/results?search_query=We+Tested+and+Compared+6+Database+Operators.+The+Results+are+In%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# We Tested and Compared 6 Database Operators. The Results are In! - Jérôme Petazzoni, Tiny Shell Script LLC & Alexandre Buisine, Enix

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Jérôme Petazzoni, Tiny Shell Script LLC, Alexandre Buisine, Enix
- Schedule: https://kccnceu2024.sched.com/event/1YeO5/we-tested-and-compared-6-database-operators-the-results-are-in-jerome-petazzoni-tiny-shell-script-llc-alexandre-buisine-enix
- Busca YouTube: https://www.youtube.com/results?search_query=We+Tested+and+Compared+6+Database+Operators.+The+Results+are+In%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre We Tested and Compared 6 Database Operators. The Results are In!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeO5/we-tested-and-compared-6-database-operators-the-results-are-in-jerome-petazzoni-tiny-shell-script-llc-alexandre-buisine-enix
- YouTube search: https://www.youtube.com/results?search_query=We+Tested+and+Compared+6+Database+Operators.+The+Results+are+In%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l33pcnQ4cUQ
- YouTube title: We Tested and Compared 6 Database Operators. The Results are In!
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/we-tested-and-compared-6-database-operators-the-results-are-in/l33pcnQ4cUQ.txt
- Transcript chars: 30333
- Keywords: operators, operator, database, actually, basically, cluster, pretty, little, backups, switch, production, manage, minutes, information, bananas, jerome, instance, restore

### Resumo baseado na transcript

[Music] good morning uh shiver M Timbers or I they say Su Artimus um so we're the Pirates and we're going to talk about database operators hi everyone can you applaud please Captain Jerome for this talk thank you so here is Jerome I'm Alex uh we actually had this talk one year ago in France at kcd France 2K 23 omage yes bagget style C Bear uh actually we had quite a lot of fun with David who was missing today uh hopefully we will present what was presented

### Excerpt da transcript

[Music] good morning uh shiver M Timbers or I they say Su Artimus um so we're the Pirates and we're going to talk about database operators hi everyone can you applaud please Captain Jerome for this talk thank you so here is Jerome I'm Alex uh we actually had this talk one year ago in France at kcd France 2K 23 omage yes bagget style C Bear uh actually we had quite a lot of fun with David who was missing today uh hopefully we will present what was presented in French last year and we will add a little bit of updates for instance we got some operators that went through releases and as well we got some kind of uh experience in production as well for based on the past 12 months so maybe J you jome you can explain us about the operators in particular sure so quick show of hands uh who knows what an operator is like a kubernetes operator yeah lots of hands cool now who knows what the database operator is uh a little bit less hand but still a lot cool so um maybe half of the folks raise their hand um so a database operator is something that lets us depro a database automatically on kubernetes and manage like the whole life cycle and Behind These fancy words we mean that it's going to take care of deploying but not just deploying the database server but like a primary a replica have backups and uh when you have backups backups are pointless if you don't have restores so also manage restoring for instance a point in time restore which is something really cool we're going to talk more about this later uh and in this Stoke we're going to uh concentrate on six operators and only SQL operators and only for pogress and myql uh it's it's not because we don't like the other one it's just because we only have like 30 something minutes so we had to constrain the scope a little bit and this is by no means an exhaustive review of all the operators out there uh again uh time constraints and so on and so on um another thing that is pretty cool with operators you know even if you are a season DBA Etc something pretty cool that you can do with database operator on kubernetes is uh leveraging local storage uh safely because you know when you are whether it's in the cloud or on Prem there is often this kind of uh dual thing am I going to use my local discs which are super fast but if I lose the machine I lose the data or am I going to use remote discs you know like EBS or SEF or something like that uh which feels safer because it's on something that is like replicated and so on but
