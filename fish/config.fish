if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Disable greeting message
set -g fish_greeting ""

# Environment path settings
set -gx PATH $PATH ~/.local/bin

# Theme settings
oh-my-posh init fish --config ~/.config/oh-my-posh/huvix.omp.json | source