using Plots

# Sigmoid helper
function sigmoid(val)
    return 1.0 / (1.0 + exp(-val))
end

function generate_transect()
    # Grid sizes
    nx = 400
    ny = 400
    x = range(-50.0, 150.0, length=nx) # km
    y = range(-1000.0, 0.0, length=ny) # m
    
    # Temperature and Saturation matrices
    # Heatmap expects matrix of size (ny, nx) or (nx, ny). In Plots.jl, heatmaps on x, y, Z expect Z of size (ny, nx) if length(x)==nx and length(y)==ny.
    # Specifically, Z[j, i] corresponds to x[i] and y[j].
    T = zeros(ny, nx)
    S = zeros(ny, nx)
    
    for j in 1:ny
        for i in 1:nx
            curr_x = x[i]
            curr_y = y[j]
            
            # 1. Surface temperature transition (land is -10 °C, ocean floor is -1.5 °C)
            T_surf = -1.5 - 8.5 * sigmoid(-curr_x / 15.0)
            
            # 2. Geothermal gradient (0.02 °C/m)
            T_bg = T_surf + 0.02 * (-curr_y)
            
            # 3. Relict permafrost anomaly centered at -300m
            sigma_y = 180.0
            y_center = -300.0
            L_decay = 70.0
            
            anomaly_x_factor = sigmoid((curr_x + 15.0) / 10.0)
            T_anomaly = -11.0 * exp(-((curr_y - y_center) / sigma_y)^2) * exp(-max(0.0, curr_x) / L_decay) * anomaly_x_factor
            
            # Combine temperature
            T_val = T_bg + T_anomaly
            T[j, i] = T_val
            
            # Ice Saturation formulation
            if T_val < -1.5
                S[j, i] = 1.0
            elseif T_val >= 0.0
                S[j, i] = 0.0
            else
                S[j, i] = -T_val / 1.5
            end
        end
    end
    
    return x, y, T, S
end

function main()
    println("Generating synthetic permafrost transect...")
    x, y, T, S = generate_transect()
    
    # Subplot 1: Temperature Field
    p1 = heatmap(x, y, T, 
                 color=cgrad(:RdYlBu, rev=true), 
                 clim=(-12.0, 16.0), 
                 title="Subsurface Temperature Field T(x, y)",
                 xlabel="Distance from Shoreline (km)",
                 ylabel="Elevation (m)",
                 colorbar_title="Temperature (°C)",
                 grid=false,
                 dpi=150)
    
    # Overlay selected isotherms
    contour!(p1, x, y, T, 
             levels=[-5.0, -2.0, -1.0, 0.0], 
             color=:black, 
             linewidth=1.2, 
             contour_labels=true)
    
    # Mark shoreline
    vline!(p1, [0.0], color=:white, linestyle=:dash, linewidth=1.5, label="Shoreline")
    
    # Subplot 2: Ice Saturation Field
    p2 = heatmap(x, y, S, 
                 color=:GnBu, 
                 clim=(0.0, 1.0), 
                 title="Ice Saturation S(x, y)",
                 xlabel="Distance from Shoreline (km)",
                 ylabel="Elevation (m)",
                 colorbar_title="Ice Saturation",
                 grid=false,
                 dpi=150)
    
    # Mark shoreline
    vline!(p2, [0.0], color=:black, linestyle=:dash, linewidth=1.5, label="Shoreline")
    
    # Combine and save
    full_plot = plot(p1, p2, layout=(2, 1), size=(800, 750))
    savefig(full_plot, "mackenzie_transect_plot.png")
    println("Success! Figure saved -> mackenzie_transect_plot.png")
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
