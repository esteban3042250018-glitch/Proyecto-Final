-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-08-2026 a las 15:58:37
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dentista`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `id` int(11) NOT NULL,
  `paciente` varchar(50) NOT NULL,
  `fecha` datetime NOT NULL,
  `doctor` varchar(50) NOT NULL,
  `procedimiento` varchar(50) NOT NULL,
  `modificaciones` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `citas`
--

INSERT INTO `citas` (`id`, `paciente`, `fecha`, `doctor`, `procedimiento`, `modificaciones`) VALUES
(1, 'JUAN', '2026-08-05 19:00:00', 'JUAN', 'LIMPIEZA', 0),
(2, 'ESTEBAN', '2025-08-24 14:30:00', 'JUAN', 'LIMPIEZA', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `doctores`
--

CREATE TABLE `doctores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(75) NOT NULL,
  `apellido` varchar(75) NOT NULL,
  `cargo` varchar(75) NOT NULL,
  `tel` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `doctores`
--

INSERT INTO `doctores` (`id`, `nombre`, `apellido`, `cargo`, `tel`) VALUES
(1, 'GUILLERMO', 'LOPEZ DORIGA', 'CIRUGIA', '2147483647'),
(2, 'SERGIO', 'ZUÑIGA', 'MAXILOFACIA', '6181234567'),
(3, 'JUAN', 'PEREZ PEREZ', 'CIRUGIA', '6189876543'),
(4, 'PEPIN', 'FLORES', 'MAXILOFACIAL', '1234567890'),
(5, 'ESTEBAN', 'AGUIRRE', 'INTELIGENTE', '1234567890');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `telefono` varchar(11) NOT NULL,
  `fecha_nac` date NOT NULL,
  `correo` varchar(100) NOT NULL,
  `tipo_sangre` varchar(3) NOT NULL,
  `procedimiento` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`id`, `nombre`, `apellido`, `telefono`, `fecha_nac`, `correo`, `tipo_sangre`, `procedimiento`) VALUES
(1, 'JUAN', 'PEREZ PEREZ', '6181234567', '2014-11-09', 'juanp@gmail.com', 'A+', 'LIMPIEZA');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `doctores`
--
ALTER TABLE `doctores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `doctores`
--
ALTER TABLE `doctores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
