---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "SDLC"
themes: ["Storage Data", "GitOps Delivery"]
speakers: ["Rotem Tamir", "Ariga"]
sched_url: https://kccncna2024.sched.com/event/1i7kw/the-hard-truth-about-gitops-and-database-rollbacks-rotem-tamir-ariga
youtube_search_url: https://www.youtube.com/results?search_query=The+Hard+Truth+About+GitOps+and+Database+Rollbacks+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Hard Truth About GitOps and Database Rollbacks - Rotem Tamir, Ariga

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[SDLC]]
- Temas: [[Storage Data]], [[GitOps Delivery]]
- País/cidade: United States / Salt Lake City
- Speakers: Rotem Tamir, Ariga
- Schedule: https://kccncna2024.sched.com/event/1i7kw/the-hard-truth-about-gitops-and-database-rollbacks-rotem-tamir-ariga
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hard+Truth+About+GitOps+and+Database+Rollbacks+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Hard Truth About GitOps and Database Rollbacks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kw/the-hard-truth-about-gitops-and-database-rollbacks-rotem-tamir-ariga
- YouTube search: https://www.youtube.com/results?search_query=The+Hard+Truth+About+GitOps+and+Database+Rollbacks+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jMJ0JSSUmd8
- YouTube title: The Hard Truth About GitOps and Database Rollbacks - Rotem Tamir, Ariga
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-hard-truth-about-gitops-and-database-rollbacks/jMJ0JSSUmd8.txt
- Transcript chars: 28096
- Keywords: database, migration, schema, version, operator, migrations, changes, application, change, called, argo, management, previous, commit, revert, happen, column, operation

### Resumo baseado na transcript

great uh hi everyone my name is RM and thank you for joining our talk today about giops rollbacks and database schema changes so before we begin a few words about myself so over the past four years I've been the CTO and co-founder of a company called arga it's part of my job I have the pleasure of being the co-maintainer of two fairly large open- Source projects the first of them is called an an is an Entity framework for go uh it was started by my co-founder

### Excerpt da transcript

great uh hi everyone my name is RM and thank you for joining our talk today about giops rollbacks and database schema changes so before we begin a few words about myself so over the past four years I've been the CTO and co-founder of a company called arga it's part of my job I have the pleasure of being the co-maintainer of two fairly large open- Source projects the first of them is called an an is an Entity framework for go uh it was started by my co-founder when he was working at Facebook today it's part of the Linux foundation and the second one is called Atlas Atlas is a database schema management tool and we will be diving a bit into it in the last portion of this talk so today we are talking about rollbacks and roll backs in the context of the people sitting in this room of software delivery is all about undoing some change or returning the system to a uh previous stable State and rollbacks are a very important capability for teams that are doing software delivery specifically when we are looking at a metric that is called mttr I'm sure many of you know about this but but to recap mttr means the mean time to recover so we deploy changes our developers uh evolve our application we deploy it to production we make configuration changes we do all sorts of stuff and at some point sometimes we have an outage we deploy a bad change it might be a configuration uh change it might be a code problem it might be something else but in any case our system is now suffering from some problem our business objectives are uh harmed by this and we want to fix it so in general we have two paths to recovering from an outage one is to tr as the issue try to look at the metrics logs traces whatever we can uh to understand what is causing the issue issue a fix deploy a new version and rejoice our problem is resolved alternatively sometimes we don't have time sometimes we don't understand the problem well enough and we just want to return to the previous known uh stable version this is called the roll back and whatever path your team chooses if we look on aggregate at the average time that it takes our team to recover from a production outage we call this the mttr and it's it's a very important metric if you want to provide good service to your a reliable service to your customers now implementing an undo button in a client side application like a word processor or a photo editor is not an easy task but it's pretty straightforward you need to keep track of the different chang
